from sqlalchemy import Column, Integer, String
from sqlalchemy.sql import func
from sqlalchemy.sql.sqltypes import TIMESTAMP

from app.database import Base


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True)
    question = Column(String, nullable=False)
    answer = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False)
    created_on_server_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=func.now()
    )

    def __repr__(self):
        return f"Question: {self.id} created at {self.created_at}"
