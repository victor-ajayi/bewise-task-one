from fastapi import APIRouter, Depends
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from utils import get_question

from app.database import get_db
from app.services import create_question

from . import schemas

root = APIRouter()


@root.post("/", status_code=201)
async def index(
    request: schemas.Request, db: Session = Depends(get_db)
) -> schemas.Response:
    while True:
        question_dict = get_question(request.questions_num)

        try:
            question = create_question(question_dict, db)
        except IntegrityError:
            continue
        else:
            break

    return question
