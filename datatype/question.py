from typing import List
from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from standard import Standard
from part import Part

class Base(DeclarativeBase):
    pass

class Question(Base):
    __tablename__ = "questions"

    questionID: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    standardID: Mapped[int] = mapped_column(ForeignKey("standards.standardID"))
    content: Mapped[str] = mapped_column(String)

    # Relationships
    standard: Mapped[Standard] = relationship(back_populates="questions")
    parts: Mapped[List[Part]] = relationship(
        back_populates="question",
        cascade="all, delete-orphan"
    )

    def __init__(self, content: str, standardID: int):
        self.content = content
        self.standardID = standardID

    def __repr__(self):
        return (
            f'<Question(questionID="{self.questionID}", '
            f'standardID="{self.standardID}", '
            f'content="{self.content}")>'
        )