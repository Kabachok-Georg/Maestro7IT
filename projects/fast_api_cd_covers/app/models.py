'''
Модели SQLAlchemy
'''

# app/models.py

from sqlalchemy import Column, Integer, String, Boolean
from .database import Base

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

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
