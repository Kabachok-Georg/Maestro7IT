'''
Pydantic схемы
'''

# app/schemas.py

from typing import Optional
from pydantic import BaseModel,  EmailStr

class GameBase(BaseModel):
    title: str
    genre: str
    release_year: int
    description: str
    photo_url: Optional[str] = None
    music_url: Optional[str] = None
    video_url: Optional[str] = None

class GameCreate(GameBase):
    pass

class GameUpdate(GameBase):
    pass

class GameInDB(GameBase):
    id: int

    class Config:
        from_attributes = True

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True
