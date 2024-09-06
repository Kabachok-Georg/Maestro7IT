'''
Основной файл FastAPI
'''
from datetime import timedelta

# app/main.py

from fastapi import FastAPI, HTTPException, Depends, Request, Form, status, utils
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.security import OAuth2PasswordRequestForm
from flask import request
from sqlalchemy.orm import Session
from typing import Optional

from . import models, schemas, crud, auth
from .auth import create_access_token
from .database import engine, SessionLocal

# Создание таблиц в базе данных
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

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

@app.get("/protected_route")
def protected_route(current_user: schemas.User = Depends(auth.get_current_user)):
    return {"message": "You are authenticated", "user": current_user}

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
    return RedirectResponse(url="/", status_code=303)

# Детальная страница игры
@app.get("/games/{game_id}", response_class=HTMLResponse)
async def read_game(request: Request, game_id: int, db: Session = Depends(get_db)):
    game = crud.get_game(db, game_id)
    if game:
        return templates.TemplateResponse("game_detail.html", {"request": request, "game": game})
    else:
        return templates.TemplateResponse("error.html", {"request": request, "error": "Игра не найдена"}, status_code=404)

# Форма редактирования игры
@app.get("/games/{game_id}/edit", response_class=HTMLResponse)
async def edit_game_form(request: Request, game_id: int, db: Session = Depends(get_db)):
    game = crud.get_game(db, game_id)
    if game:
        return templates.TemplateResponse("edit_game.html", {"request": request, "game": game})
    else:
        return templates.TemplateResponse("error.html", {"request": request, "error": "Игра не найдена"}, status_code=404)

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
    if updated_game:
        return RedirectResponse(url=f"/games/{game_id}", status_code=303)
    else:
        return templates.TemplateResponse("error.html", {"request": request, "error": "Игра не найдена"}, status_code=404)

# Обработчик удаления игры
@app.post("/games/{game_id}/delete", response_class=HTMLResponse)
async def delete_game(game_id: int, db: Session = Depends(get_db)):
    deleted_game = crud.delete_game(db, game_id)
    if deleted_game:
        return RedirectResponse(url="/", status_code=303)
    else:
        return templates.TemplateResponse("error.html", {"request": request, "error": "Игра не найдена"}, status_code=404)


# Форма регистрации нового пользователя
@app.get("/register", response_class=HTMLResponse)
async def register_form(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


@app.post("/register", response_class=HTMLResponse)
async def register_user(request: Request, db: Session = Depends(get_db),
                        username: str = Form(...), password: str = Form(...),
                        password_repeat: str = Form(...)):
    if password != password_repeat:
        return templates.TemplateResponse("register.html", {"request": request, "error": "Пароли не совпадают"})

    user = crud.get_user_by_username(db, username=username)
    if user:
        return templates.TemplateResponse("register.html", {"request": request, "error": "Пользователь уже существует"})

    hashed_password = utils.hash_password(password)
    crud.create_user(db, schemas.UserCreate(username=username, password=hashed_password))
    return RedirectResponse(url="/login", status_code=303)


# Форма аутентификации пользователя
@app.get("/login", response_class=HTMLResponse)
async def login_form(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = crud.get_user_by_username(db, username=form_data.username)
    if not user or not utils.verify_password(form_data.password, user.password):
        raise HTTPException(status_code=401, detail="Неверное имя пользователя или пароль")

    access_token_expires = timedelta(minutes=15)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}