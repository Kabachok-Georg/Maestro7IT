import os
import json
import random
from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from projects.fast_api_cd_covers.app.models import Base, Game, Comment  # Импортируем модели

# Настройка базы данных
DATABASE_URL = "sqlite:///../games.db"  # Путь к базе данных в корневой папке проекта
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

fake = Faker()

def generate_comments(num_comments=10, file_path="generate_data/comments.json"):
    db = SessionLocal()
    try:
        # Получаем все игры из базы данных
        games = db.query(Game).all()

        if not games:
            print("Нет игр в базе данных.")
            return

        comments = []
        for _ in range(num_comments):
            comment = {
                "game_id": random.choice(games).id,  # Случайная игра
                "author": fake.name(),  # Случайный автор
                "content": fake.text(),  # Содержание комментария
                "rating": random.randint(1, 10)  # Случайный рейтинг от 1 до 10
            }
            comments.append(comment)

        # Сохраняем данные в JSON файл
        os.makedirs(os.path.dirname(file_path), exist_ok=True)  # Создаем папку, если она не существует
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(comments, f, ensure_ascii=False, indent=4)

        print(f"Генерация {num_comments} комментариев завершена. Данные сохранены в {file_path}.")
    finally:
        db.close()

def load_comments_from_json(file_path="generate_data/comments.json"):
    db = SessionLocal()
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            comments_data = json.load(f)

        for comment_data in comments_data:
            new_comment = Comment(**comment_data)
            db.add(new_comment)

        db.commit()
        print(f"Комментарии из {file_path} успешно загружены в базу данных.")
    finally:
        db.close()

if __name__ == "__main__":
    generate_comments(num_comments=10)  # Генерация и сохранение комментариев
    load_comments_from_json()  # Загрузка комментариев из JSON в базу данных
