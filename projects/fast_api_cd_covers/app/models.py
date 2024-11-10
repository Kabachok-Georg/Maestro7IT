from sqlalchemy import Column, Integer, String, Boolean, Text, ForeignKey, DateTime, func, UniqueConstraint
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    # Связь с рейтингами
    ratings = relationship("Rating", back_populates="user")

    # Связь с избранными играми
    favorite_games = relationship("FavoriteGame", back_populates="user")

class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    genre = Column(String, nullable=False)
    release_year = Column(Integer, nullable=False)
    description = Column(String, nullable=False)
    photo_url = Column(String, nullable=True)
    music_url = Column(String, nullable=True)
    video_url = Column(String, nullable=True)

    # Рейтинг проекта по 10-балльной шкале
    rating = Column(Integer, nullable=True)

    # Связь с комментариями
    comments = relationship("Comment", back_populates="game")

    # Связь с рейтингами
    ratings = relationship("Rating", back_populates="game")

    # Связь с избранными играми
    favorite_games = relationship("FavoriteGame", back_populates="game")

class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    game_id = Column(Integer, ForeignKey("games.id"))
    author = Column(String, nullable=False)
    content = Column(Text, nullable=False)

    # Рейтинг проекта по 10-балльной шкале
    rating = Column(Integer, nullable=True)

    # Связь с игрой
    game = relationship("Game", back_populates="comments")

class FavoriteGame(Base):
    __tablename__ = "favorite_games"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True)
    game_id = Column(Integer, ForeignKey("games.id"), index=True)

    user = relationship("User", back_populates="favorite_games")
    game = relationship("Game", back_populates="favorite_games")

    __table_args__ = (
        UniqueConstraint('user_id', 'game_id', name='unique_user_game'),
    )

class Rating(Base):
    __tablename__ = "ratings"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True)
    game_id = Column(Integer, ForeignKey("games.id"), index=True)
    rating = Column(Integer, nullable=False)

    user = relationship("User", back_populates="ratings")
    game = relationship("Game", back_populates="ratings")

    __table_args__ = (
        UniqueConstraint('user_id', 'game_id', name='unique_user_game_rating'),  # Уникальная комбинация пользователь-игра
    )
