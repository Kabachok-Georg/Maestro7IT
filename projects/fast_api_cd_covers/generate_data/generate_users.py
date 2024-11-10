import json
import os
from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from projects.fast_api_cd_covers.app.models import Base, User  # Импортируем модели
from projects.fast_api_cd_covers.app.utils import hash_password  # Импортируем функцию хеширования

# Настройка базы данных
DATABASE_URL = "sqlite:///../games.db"  # Путь к базе данных в корневой папке проекта
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

fake = Faker()

def generate_users(num_users=10, file_path="generate_data/users.json"):
    """Генерация пользователей и сохранение их в JSON файл."""
    # Создаем директорию, если она не существует
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    db = SessionLocal()
    try:
        users = []
        for _ in range(num_users):
            user = {
                "username": fake.user_name(),
                "email": fake.email(),
                "hashed_password": hash_password(fake.password()),  # Хешируем пароль
                "is_active": True
            }
            users.append(user)

        # Сохраняем данные в JSON файл
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(users, f, ensure_ascii=False, indent=4)

        print(f"Генерация {num_users} пользователей завершена. Данные сохранены в {file_path}.")
    finally:
        db.close()

def load_users_from_json(file_path="generate_data/users.json"):
    """Загрузка пользователей из JSON файла в базу данных."""
    db = SessionLocal()
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            users_data = json.load(f)

        for user_data in users_data:
            # Проверка на существование пользователя с таким же username или email
            existing_user = db.query(User).filter(
                (User.username == user_data['username']) | (User.email == user_data['email'])
            ).first()
            if existing_user:
                print(f"Пользователь с именем {user_data['username']} или email {user_data['email']} уже существует.")
                continue  # Пропускаем этого пользователя

            # Создание нового пользователя
            new_user = User(**user_data)
            db.add(new_user)

        db.commit()
        print(f"Пользователи из {file_path} успешно загружены в базу данных.")
    finally:
        db.close()

if __name__ == "__main__":
    generate_users(num_users=10)  # Генерация и сохранение пользователей
    load_users_from_json()  # Загрузка пользователей из JSON в базу данных
