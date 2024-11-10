'''
CRUD операции
'''
# app/crud.py

from sqlalchemy.orm import Session
from . import models, schemas, utils
from typing import Optional
from .models import FavoriteGame, User, Game, Comment
from fastapi import HTTPException

def get_game(db: Session, game_id: int):
    return db.query(models.Game).filter(models.Game.id == game_id).first()

def create_game(db: Session, game: schemas.GameCreate):
    # Проверяем, существует ли игра с таким же заголовком
    existing_game = db.query(models.Game).filter(models.Game.title == game.title).first()
    if existing_game:
        raise HTTPException(status_code=400, detail="Игра с таким заголовком уже существует")

    db_game = models.Game(
        title=game.title,
        genre=game.genre,
        release_year=game.release_year,
        description=game.description,
        photo_url=game.photo_url,
        music_url=game.music_url,
        video_url=game.video_url
    )
    db.add(db_game)
    db.commit()
    db.refresh(db_game)
    return db_game

def update_game(db: Session, game_id: int, game: schemas.GameUpdate):
    db_game = get_game(db, game_id)
    if db_game:
        db_game.title = game.title
        db_game.genre = game.genre
        db_game.release_year = game.release_year
        db_game.description = game.description
        db_game.photo_url = game.photo_url
        db_game.music_url = game.music_url
        db_game.video_url = game.video_url
        db.commit()
        db.refresh(db_game)
    return db_game

def delete_game(db: Session, game_id: int):
    db_game = get_game(db, game_id)
    if db_game:
        db.delete(db_game)
        db.commit()
    return db_game

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = utils.hash_password(user.password)
    db_user = models.User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def get_games(db: Session, title: Optional[str] = None, release_year: Optional[int] = None):
    query = db.query(models.Game)

    if title:
        query = query.filter(models.Game.title.ilike(f"%{title}%"))
    if release_year is not None:  # Проверяем на None вместо True
        query = query.filter(models.Game.release_year == release_year)

    return query.all()


def add_to_favorites(db: Session, user_id: int, game_id: int):
    existing_favorite = db.query(FavoriteGame).filter(FavoriteGame.user_id == user_id, FavoriteGame.game_id == game_id).first()

    if existing_favorite:
        return existing_favorite  # Или выбросьте исключение

    favorite = FavoriteGame(user_id=user_id, game_id=game_id)
    db.add(favorite)
    db.commit()
    db.refresh(favorite)
    return favorite


def remove_from_favorites(db: Session, user_id: int, game_id: int):
    favorite = db.query(FavoriteGame).filter(
        FavoriteGame.user_id == user_id,
        FavoriteGame.game_id == game_id
    ).first()

    if favorite:
        db.delete(favorite)
        db.commit()
    return favorite


def get_favorites(db: Session, user_id: int):
    # Получаем все избранные игры для данного пользователя
    favorites = db.query(models.FavoriteGame).filter(models.FavoriteGame.user_id == user_id).all()

    # Извлекаем информацию о каждой игре по ее ID
    games = []
    for favorite in favorites:
        game = db.query(models.Game).filter(models.Game.id == favorite.game_id).first()
        if game:
            games.append(game)

    return games

def add_rating(db: Session, rating: schemas.RatingCreate, game_id: int, user_id: int):
    db_rating = models.Rating(value=rating.value, game_id=game_id, user_id=user_id)
    db.add(db_rating)
    db.commit()
    db.refresh(db_rating)
    return db_rating

def get_average_rating(db: Session, game_id: int):
    ratings = db.query(models.Rating).filter(models.Rating.game_id == game_id).all()
    if ratings:
        avg_rating = sum(rating.value for rating in ratings) / len(ratings)
        return avg_rating
    return None
