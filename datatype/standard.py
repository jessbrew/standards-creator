from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Standard(Base):
    __tablename__ = "standards"

    standardID = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    standardNumber = Column(Integer, nullable=False)
    courseID = Column(Integer, nullable=False)

    # Proper relationship declaration
    questions = relationship("Question", back_populates="standard", cascade="all, delete-orphan")

    def __init__(self, name, number, courseID):
        self.standardNumber = number
        self.name = name
        self.courseID = courseID

    def __repr__(self):
        return (
            f'<Standard(standardID="{self.standardID}", '
            f'name="{self.name}", '
            f'standardNumber="{self.standardNumber}", '
            f'courseID="{self.courseID}")>'
        )