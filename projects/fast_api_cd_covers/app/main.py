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

from .models import Game, Comment, Rating
from .utils import hash_password, verify_password
from . import models, schemas, crud, auth
from .auth import create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES
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
async def read_root(
        request: Request,
        title: Optional[str] = None,
        release_year: Optional[str] = None,
        db: Session = Depends(get_db)
):
    release_year_int = int(release_year) if release_year else None
    if title is None and release_year_int is None:
        games = crud.get_games(db)  # Получаем все игры
    else:
        games = crud.get_games(db, title=title, release_year=release_year_int)

    return templates.TemplateResponse("index.html", {"request": request, "games": games})


# Форма добавления новой игры
@app.get("/add", response_class=HTMLResponse)
async def add_game_form(request: Request):
    return templates.TemplateResponse("add_game.html", {"request": request})


# Пример функции для добавления игры с улучшенным логированием
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
    try:
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
    except Exception as e:
        logger.error(f"Ошибка при добавлении игры: {e}")
        raise HTTPException(status_code=500, detail="Ошибка при добавлении игры")


# Пример улучшенной функции для получения данных о игре с обработкой ошибок
@app.get("/games/{game_id}", response_class=HTMLResponse)
async def read_game(request: Request, game_id: int, db: Session = Depends(get_db)):
    try:
        game = crud.get_game(db, game_id)
        if not game:
            logger.warning(f"Игра с ID {game_id} не найдена")
            return templates.TemplateResponse("error.html", {"request": request, "error": "Игра не найдена"}, status_code=404)
        return templates.TemplateResponse("game_detail.html", {"request": request, "game": game})
    except Exception as e:
        logger.error(f"Ошибка при получении игры с ID {game_id}: {e}")
        raise HTTPException(status_code=500, detail="Ошибка сервера")


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
async def delete_game(request: Request, game_id: int, db: Session = Depends(get_db)):
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
    password_repeat: str = Form(...),
):
    if password != password_repeat:
        return templates.TemplateResponse("register.html", {"request": request, "error": "Пароли не совпадают"})

    user = crud.get_user_by_username(db, username=username)
    if user:
        return templates.TemplateResponse("register.html", {"request": request, "error": "Пользователь уже существует"})

    hashed_password = hash_password(password)  # Используем функцию из utils.py
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

    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Неверное имя пользователя или пароль")

    if not verify_password(form_data.password, user.hashed_password):  # Используем функцию из utils.py
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Неверное имя пользователя или пароль")

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user.username}, expires_delta=access_token_expires)

    return {"access_token": access_token, "token_type": "bearer"}


# Обработчик добавления игры в избранное
@app.post("/games/{game_id}/favorite")
async def favorite_game(
    game_id: int,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(auth.get_current_user)
):
    # Проверка существования игры в базе данных
    game = crud.get_game(db, game_id)
    if game is None:
        logger.warning(f"Игра с ID {game_id} не найдена")
        raise HTTPException(status_code=404, detail="Игра не найдена")

    # Добавление игры в избранное пользователя
    crud.add_game_to_favorites(db=db, user_id=current_user.id, game_id=game_id)
    logger.info(f"Игра с ID {game_id} добавлена в избранное пользователем {current_user.username}")
    return RedirectResponse(url=f"/games/{game_id}", status_code=303)


@app.get("/games/{game_id}", response_class=HTMLResponse)
async def read_game(game_id: int, db: Session = Depends(get_db)):
    game = db.query(Game).filter(Game.id == game_id).first()
    if game is None:
        raise HTTPException(status_code=404, detail="Game not found")
    comments = db.query(Comment).filter(Comment.game_id == game_id).all()
    return templates.TemplateResponse("game_detail.html", {"request": {}, "game": game, "comments": comments})

@app.post("/games/{game_id}/comment")
async def add_comment(game_id: int, author: str = Form(...), content: str = Form(...), rating: int = Form(0), db: Session = Depends(get_db)):
    game = db.query(Game).filter(Game.id == game_id).first()
    if game is None:
        raise HTTPException(status_code=404, detail="Game not found")

    new_comment = Comment(author=author, content=content, rating=rating, game_id=game_id)
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return {"message": "Comment added successfully"}
