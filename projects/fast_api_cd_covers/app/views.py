from fastapi import APIRouter, Request, RedirectResponse
from .models import Comment
from .database import SessionLocal

router = APIRouter()


@router.post("/games/{game_id}/comment")
async def add_comment(request: Request, game_id: int):
    form = await request.form()
    author = form.get("author")
    content = form.get("content")

    if author and content:
        db = SessionLocal()
        comment = Comment(author=author, content=content, game_id=game_id)
        db.add(comment)
        db.commit()
        db.refresh(comment)
        db.close()

    return RedirectResponse(f"/games/{game_id}", status_code=303)
