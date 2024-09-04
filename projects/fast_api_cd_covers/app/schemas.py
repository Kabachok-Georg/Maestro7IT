'''
Pydantic схемы
'''

# app/schemas.py

from typing import Optional
from pydantic import BaseModel

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
