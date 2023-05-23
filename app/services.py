from sqlalchemy.orm import Session

from . import models


def create_question(data: dict, db: Session) -> models.Question:
    question = db.query(models.Question).filter_by(id=data["id"]).first()

    question = models.Question(**data)

    db.add(question)
    db.commit()
    db.refresh(question)

    return question
