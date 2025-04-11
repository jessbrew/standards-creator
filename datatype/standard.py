from __future__ import annotations
from typing import List
from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship

Base = declarative_base()

class Standard(Base):
    __tablename__ = "Standard"

    standardID: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    standardNumber: Mapped[int] = mapped_column(Integer, nullable=False)
    courseID: Mapped[int] = mapped_column(Integer, nullable=False)

    # Fixed relationship to Question
    questions: Mapped[List[Question]] = relationship(
        "Question",
        back_populates="standard",
        cascade="all, delete-orphan"
    )

    def __init__(self, name: str, number: int, courseID: int):
        self.name = name
        self.standardNumber = number
        self.courseID = courseID

    def __repr__(self):
        return (
            f'<Standard(standardID="{self.standardID}", '
            f'name="{self.name}", '
            f'standardNumber="{self.standardNumber}", '
            f'courseID="{self.courseID}")>'
        )


class Question(Base):
    __tablename__ = "Question"

    questionID: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    standardID: Mapped[int] = mapped_column(ForeignKey("Standard.standardID"), nullable=False)
    content: Mapped[str] = mapped_column(String, nullable=False)

    # Fixed reverse relationship to Standard
    standard: Mapped[Standard] = relationship(
        "Standard",
        back_populates="questions"
    )

    parts: Mapped[List[Part]] = relationship(
        "Part",
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


class Part(Base):
    __tablename__ = "Part"

    partID: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    questionID: Mapped[int] = mapped_column(ForeignKey("Question.questionID"), nullable=False)
    content: Mapped[str] = mapped_column(String, nullable=False)

    # Fixed reverse relationship to Question
    question: Mapped[Question] = relationship(
        "Question",
        back_populates="parts"
    )

    def __init__(self, content: str, questionID: int):
        self.content = content
        self.questionID = questionID

    def __repr__(self):
        return (
            f'<Part(partID="{self.partID}", '
            f'questionID="{self.questionID}", '
            f'content="{self.content}")>'
        )
