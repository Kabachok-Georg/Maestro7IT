# load_data.py

import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from projects.fast_api_cd_covers.app.models import Game
from projects.fast_api_cd_covers.app.schemas import GameCreate

# Замените строку подключения на вашу
DATABASE_URL = "sqlite:///./games.db"

# Создаем соединение с базой данных
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def load_data_from_json(json_file: str):
    # Создаем сессию базы данных
    db = SessionLocal()

    # Открываем JSON файл
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Проходим по каждому элементу в JSON
    for item in data:
        # Проверяем, есть ли поле photo_url
        if 'photo_url' not in item:
            item['photo_url'] = None  # Если поле отсутствует, устанавливаем его значение в None

        # Создаем объект GameCreate из данных
        game_data = GameCreate(
            title=item.get('title'),
            genre=item.get('genre'),
            release_year=item.get('release_year'),
            description=item.get('description'),
            photo_url=item.get('photo_url'),
            music_url=item.get('music_url'),
            video_url=item.get('video_url')
        )

        # Добавляем данные в базу
        db_game = Game(
            title=game_data.title,
            genre=game_data.genre,
            release_year=game_data.release_year,
            description=game_data.description,
            photo_url=game_data.photo_url,
            music_url=game_data.music_url,
            video_url=game_data.video_url
        )

        db.add(db_game)

    # Сохраняем изменения в базе данных
    db.commit()
    db.close()


if __name__ == "__main__":
    # Замените 'data.json' на путь к вашему JSON файлу
    load_data_from_json('data.json')
