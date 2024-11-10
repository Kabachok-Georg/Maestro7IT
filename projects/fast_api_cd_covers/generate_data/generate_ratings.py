import random
import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from projects.fast_api_cd_covers.app.models import Game, Rating  # Предполагается, что Rating - это модель для рейтингов в базе данных
from projects.fast_api_cd_covers.app.utils import hash_password  # Из utils.py для хэширования паролей, если нужно
from sqlalchemy.exc import IntegrityError

# Настройки базы данных
DATABASE_URL = "sqlite:///../games.db"  # Путь к базе данных в корневой папке проекта

# Создание подключения к базе данных
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Функция для генерации случайных рейтингов и их сохранения в базе данных
def generate_random_ratings(num_ratings: int):
    ratings = []
    for _ in range(num_ratings):
        user_id = random.randint(1, 10)  # Пример ID пользователей (можно настроить)
        game_id = random.randint(1, 5)  # Пример ID игр (можно настроить)
        rating_value = random.randint(1, 5)  # Рейтинг от 1 до 5

        ratings.append({
            "user_id": user_id,
            "game_id": game_id,
            "rating": rating_value
        })

    # Сохранение в файл JSON
    with open("generate_data/ratings.json", "w") as f:
        json.dump(ratings, f, indent=4)

    print(f"Генерация {num_ratings} рейтингов завершена. Данные сохранены в ratings.json.")


# Функция для загрузки рейтингов из JSON в базу данных
def load_ratings_from_json():
    # Открываем файл с рейтингами
    with open("generate_data/ratings.json", "r") as f:
        ratings_data = json.load(f)

    # Создаем сессию для работы с базой данных
    db = SessionLocal()

    for rating_data in ratings_data:
        user_id = rating_data["user_id"]
        game_id = rating_data["game_id"]
        rating_value = rating_data["rating"]

        # Попробуем найти существующий рейтинг для данного пользователя и игры
        existing_rating = db.query(Rating).filter_by(user_id=user_id, game_id=game_id).first()

        if existing_rating:
            # Если рейтинг существует, обновим его
            existing_rating.rating = rating_value
            print(f"Рейтинг обновлен для пользователя {user_id} и игры {game_id}.")
        else:
            # Если рейтинга нет, добавляем новый
            new_rating = Rating(user_id=user_id, game_id=game_id, rating=rating_value)
            try:
                db.add(new_rating)
                db.commit()
                print(f"Новый рейтинг добавлен для пользователя {user_id} и игры {game_id}.")
            except IntegrityError:
                db.rollback()
                print(f"Ошибка при добавлении рейтинга для пользователя {user_id} и игры {game_id}.")

    db.close()


if __name__ == "__main__":
    # Генерируем 10 случайных рейтингов
    generate_random_ratings(10)

    # Загружаем данные из JSON в базу данных
    load_ratings_from_json()
