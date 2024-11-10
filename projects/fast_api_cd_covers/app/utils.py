from sqlalchemy import func
from .models import Game, Comment
from sqlalchemy.orm import Session
from passlib.context import CryptContext

# Инициализация контекста для хэширования паролей
pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")

def hash_password(password: str) -> str:
    """Хэширование пароля"""
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Проверка пароля"""
    return pwd_context.verify(plain_password, hashed_password)

def update_game_rating(game_id: int, db: Session):
    """Вычисление и обновление среднего рейтинга игры на основе комментариев"""
    # Получаем игру по ID
    game = db.query(Game).filter(Game.id == game_id).first()
    if not game:
        return None

    # Рассчитываем средний рейтинг по комментариям
    average_rating = db.query(func.avg(Comment.rating)).filter(Comment.game_id == game.id).scalar()

    if average_rating is not None:
        # Обновляем рейтинг игры (округляем до целого числа)
        rounded_rating = round(average_rating)
        if game.rating != rounded_rating:
            game.rating = rounded_rating
            db.commit()
            db.refresh(game)
            return game
    return None
