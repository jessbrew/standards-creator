from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from question import Question

class Base(DeclarativeBase):
    pass

class Part(Base):
    __tablename__ = "parts"

    partID: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    questionID: Mapped[int] = mapped_column(ForeignKey("questions.questionID"))
    content: Mapped[str] = mapped_column(String)

    # Relationship to Question
    question: Mapped[Question] = relationship(back_populates="parts")

    def __init__(self, content: str, questionID: int):
        self.content = content
        self.questionID = questionID

    def __repr__(self):
        return (
            f'<Part(partID="{self.partID}", '
            f'questionID="{self.questionID}", '
            f'content="{self.content}")>'
        )