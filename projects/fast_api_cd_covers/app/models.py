from sqlalchemy import Column, Integer, String, Boolean, Text, ForeignKey, DateTime, func, UniqueConstraint
from .database import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

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

    # Связь с комментариями
    comments = relationship("Comment", back_populates="game")
    # Связь с избранными играми
    favorite_games = relationship("FavoriteGame", back_populates="game")

class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    game_id = Column(Integer, ForeignKey("games.id"))
    author = Column(String, nullable=False)
    content = Column(Text, nullable=False)

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
