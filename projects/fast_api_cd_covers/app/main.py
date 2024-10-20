'''
Основной файл FastAPI
'''

from datetime import timedelta
from typing import Optional

from fastapi import FastAPI, HTTPException, Depends, Request, Form, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.orm import Session

from .utils import hash_password, verify_password
from . import models, schemas, crud, auth
from .auth import create_access_token
from .database import engine, SessionLocal, get_db

import logging

# Создание таблиц в базе данных
models.Base.metadata.create_all(bind=engine)

# Настройка приложения и логирования
app = FastAPI()
logger = logging.getLogger(__name__)

# Подключение статических файлов
app.mount("/static", StaticFiles(directory="static"), name="static")

# Настройка шаблонов
templates = Jinja2Templates(directory="templates")

# Dependency для получения сессии базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Приватный роут с авторизацией
@app.get("/protected_route")
def protected_route(current_user: schemas.User = Depends(auth.get_current_user)):
    return {"message": "Вы аутентифицированы", "user": current_user}


# Главная страница - список игр
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request, db: Session = Depends(get_db)):
    games = crud.get_games(db)
    return templates.TemplateResponse("index.html", {"request": request, "games": games})


# Форма добавления новой игры
@app.get("/add", response_class=HTMLResponse)
async def add_game_form(request: Request):
    return templates.TemplateResponse("add_game.html", {"request": request})


# Обработчик добавления новой игры
@app.post("/add", response_class=HTMLResponse)
async def create_game(
    request: Request,
    db: Session = Depends(get_db),
    title: str = Form(...),
    genre: str = Form(...),
    release_year: int = Form(...),
    description: str = Form(...),
    photo_url: Optional[str] = Form(None),
    music_url: Optional[str] = Form(None),
    video_url: Optional[str] = Form(None)
):
    new_game = schemas.GameCreate(
        title=title,
        genre=genre,
        release_year=release_year,
        description=description,
        photo_url=photo_url,
        music_url=music_url,
        video_url=video_url
    )
    crud.create_game(db=db, game=new_game)
    logger.info(f"Игра {title} добавлена")
    return RedirectResponse(url="/", status_code=303)


# Детальная страница игры
@app.get("/games/{game_id}", response_class=HTMLResponse)
async def read_game(request: Request, game_id: int, db: Session = Depends(get_db)):
    game = crud.get_game(db, game_id)
    if not game:
        logger.warning(f"Игра с ID {game_id} не найдена")
        return templates.TemplateResponse("error.html", {"request": request, "error": "Игра не найдена"}, status_code=404)
    return templates.TemplateResponse("game_detail.html", {"request": request, "game": game})


# Форма редактирования игры
@app.get("/games/{game_id}/edit", response_class=HTMLResponse)
async def edit_game_form(request: Request, game_id: int, db: Session = Depends(get_db)):
    game = crud.get_game(db, game_id)
    if not game:
        logger.warning(f"Игра с ID {game_id} не найдена для редактирования")
        return templates.TemplateResponse("error.html", {"request": request, "error": "Игра не найдена"}, status_code=404)
    return templates.TemplateResponse("edit_game.html", {"request": request, "game": game})


# Обработчик обновления игры
@app.post("/games/{game_id}/edit", response_class=HTMLResponse)
async def update_game(
    request: Request,
    game_id: int,
    db: Session = Depends(get_db),
    title: str = Form(...),
    genre: str = Form(...),
    release_year: int = Form(...),
    description: str = Form(...),
    photo_url: Optional[str] = Form(None),
    music_url: Optional[str] = Form(None),
    video_url: Optional[str] = Form(None)
):
    game_data = schemas.GameUpdate(
        title=title,
        genre=genre,
        release_year=release_year,
        description=description,
        photo_url=photo_url,
        music_url=music_url,
        video_url=video_url
    )
    updated_game = crud.update_game(db, game_id, game_data)
    if not updated_game:
        logger.warning(f"Ошибка обновления: игра с ID {game_id} не найдена")
        return templates.TemplateResponse("error.html", {"request": request, "error": "Игра не найдена"}, status_code=404)

    logger.info(f"Игра с ID {game_id} успешно обновлена")
    return RedirectResponse(url=f"/games/{game_id}", status_code=303)


# Обработчик удаления игры
@app.post("/games/{game_id}/delete", response_class=HTMLResponse)
async def delete_game(game_id: int, db: Session = Depends(get_db)):
    deleted_game = crud.delete_game(db, game_id)
    if not deleted_game:
        logger.warning(f"Ошибка удаления: игра с ID {game_id} не найдена")
        return templates.TemplateResponse("error.html", {"request": request, "error": "Игра не найдена"}, status_code=404)

    logger.info(f"Игра с ID {game_id} успешно удалена")
    return RedirectResponse(url="/", status_code=303)


# Регистрация нового пользователя
@app.get("/register", response_class=HTMLResponse)
async def register_form(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


@app.post("/register", response_class=HTMLResponse)
async def register_user(
    request: Request,
    db: Session = Depends(get_db),
    username: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    password_repeat: str = Form(...)
):
    if password != password_repeat:
        return templates.TemplateResponse("register.html", {"request": request, "error": "Пароли не совпадают"})

    user = crud.get_user_by_username(db, username=username)
    if user:
        return templates.TemplateResponse("register.html", {"request": request, "error": "Пользователь уже существует"})

    hashed_password = hash_password(password)
    crud.create_user(db, schemas.UserCreate(username=username, email=email, password=hashed_password))
    logger.info(f"Пользователь {username} зарегистрирован")
    return RedirectResponse(url="/login", status_code=303)


# Аутентификация пользователя
@app.get("/login", response_class=HTMLResponse)
async def login_form(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = crud.get_user_by_username(db, username=form_data.username)

    if not user:
        logger.warning("Пользователь не найден")
        raise HTTPException(status_code=401, detail="Неверное имя пользователя или пароль")

    if not verify_password(form_data.password, user.hashed_password):
        logger.warning("Ошибка проверки пароля")
        raise HTTPException(status_code=401, detail="Неверное имя пользователя или пароль")

    access_token_expires = timedelta(minutes=15)
    access_token = create_access_token(data={"sub": user.username}, expires_delta=access_token_expires)
    logger.info(f"Пользователь {user.username} успешно вошел")

    return {"access_token": access_token, "token_type": "bearer"}
