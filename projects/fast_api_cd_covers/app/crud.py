'''
CRUD операции
'''
# app/crud.py

from sqlalchemy.orm import Session
from . import models, schemas, utils
from typing import Optional

def get_game(db: Session, game_id: int):
    return db.query(models.Game).filter(models.Game.id == game_id).first()

def create_game(db: Session, game: schemas.GameCreate):
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

