# Библиотека игровых проектов на Fast API (добавление в избранное) 

![img.png](img/fast_api.png)

![img.png](img/index_v1.png)

![edit_game_detail.png](img/edit_game_detail.png)

![add_game_detail.png](img/add_game_detail.png)

## Описание проекта:

Создадим полноценное веб-приложение с использованием FastAPI и Bootstrap.

Мы будем использовать FastAPI для создания API и рендеринга HTML-шаблонов с помощью Jinja2 для отображения дисков PS4, Xbox, Nintendo ...

Bootstrap будет использоваться для стилизации нашего сайта.

## Структура проекта:
```
fast_api_cd_covers/
│
├── app/
│   ├── __init__.py         # Инициализация приложения
│   ├── main.py             # Основной файл FastAPI с роутами и конфигурацией
│   ├── crud.py             # Операции с базой данных
│   ├── models.py           # Модели базы данных SQLAlchemy
│   ├── schemas.py          # Схемы Pydantic для валидации данных
│   ├── auth.py             # JWT и логика аутентификации
│   ├── utils.py            # Хэширование паролей
│   └── database.py         # Настройка базы данных (SQLAlchemy)
│
├── templates/              # Папка с HTML-шаблонами
│   ├── index.html          # Главная страница со списком игр
│   ├── game.html           # Страница подробной информации об игре
│   ├── game_detail.html    # Детальная информация об игре
│   ├── base.html           # Базовый шаблон HTML
│   ├── add_game.html       # Форма для добавления новой игры
│   ├── edit_game.html      # Изменение информации об игре
│   └── error.html          # Страница 404
│
├── static/                 # Папка со статическими файлами
│   ├── css/
│   │   └── bootstrap.min.css # Bootstrap CSS
│   ├── images/
│   │    ├── image_1.jpg
│   │    ├── image_2.jpg
│   │    └── image_3.jpg
│   ├── js/
│   │   └── bootstrap.bundle.min.js # Bootstrap JS
│   └── music/
│       ├── music_1.mp3
│       ├── music_2.mp3
│       └── music_3.mp3
│
├── .gitignore              # Файл .gitignore
├── .env                    # Конфигурация секретных ключей
├── data.json               # Файл с данными в формате JSON
├── games.db                # База данных
├── load_data.py            # Функция для загрузки данных в BD
├── requirements.txt        # Файл зависимостей
└── README.md               # Файл с описанием проекта
```

```
games - Это массив, содержащий объекты, каждый из которых представляет собой игру.
        id: Уникальный идентификатор игры.
        title: Название игры.
        genre: Жанр игры.
        release_year: Год выпуска игры.
        description: Краткое описание игры.
        photo_url: URL изображения обложки игры.
        music_url: URL аудиофайла с музыкой из игры.
        video_url: URL видеофайла с трейлером или другим видео о игре.
```

```
✔ Uncharted 4: A Thief’s End
✔ Horizon: Zero Dawn
✔ Detroit: Become Human
✔ Marvel’s Spider-Man
✔ Red Dead Redemption 2
✔ Ratchet & Clank
✔ Mass Effect: Legendary Edition
✔ Gran Turismo 7
✔ The Last Guardian™
✔ God of War
✔ Final Fantasy VII Remake
✔ Bloodborne
✔ Persona 5
```

## Запуск проекта

Установка зависимостей:
```
`pip install -r requirements.txt`
pip install fastapi sqlalchemy passlib bcrypt jose uvicorn
```

Запустите FastAPI приложение с помощью Uvicorn:
```
`uvicorn app.main:app # --reload`
```

Главная страница Fast API:
```
http://127.0.0.1:8000/docs
http://127.0.0.1:8000/games
http://127.0.0.1:8000/games/{game_id}
http://127.0.0.1:8000/games/{game_id}/delete
```

```
Теперь проект полностью готов и организован.
Вы можете запустить приложение и проверить его функциональность по указанным инструкциям.
```

**Преподаватель:** Дуплей Максим Игоревич

**Студент:** Данилов Георгий Алексеевич

**Дата:** 30.08.2024
