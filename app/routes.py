from fastapi import APIRouter, Depends
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.question import Question
from app.services import save_question

from . import schemas
from .utils import get_question

root = APIRouter()


@root.post("/", status_code=201)
async def index(
    request: schemas.Request, db: Session = Depends(get_db)
) -> schemas.Response:
    questions: list[dict] = get_question(request.questions_num)

    for i in range(request.questions_num):
        question = questions[i]
        while True:
            try:
                save_question(question, db)
            except IntegrityError:
                question = get_question(1)
            else:
                break

    last_question = (
        db.query(Question)
        .order_by(Question.created_on_server_at.desc())
        .limit(1)
        .first()
    )

    return last_question
