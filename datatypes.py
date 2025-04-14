from __future__ import annotations
from typing import List
from sqlalchemy import String, Integer, ForeignKey, Column
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

class Course(Base):
    __tablename__ = "Course"

    courseID = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    semester = Column(String)
    courseCode = Column(String)

    def __init__(self, courseID, name, semester, courseCode):
        self.courseID = courseID
        self.name = name
        self.semester = semester
        self.courseCode = courseCode

    def __repr__(self):
        return f'<Course (courseID="{self.courseID}", name="{self.name}", semester="{self.semester}", courseCode="{self.courseCode}")>'

class Formula(Base):
    __tablename__ = "Formula"

    formulaID = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    content = Column(String)

    def __init__(self, formulaID, name, content):
        self.formulaID = formulaID
        self.name = name
        self.content = content

    def __repr__(self):
        return f'<Formula (formulaID="{self.formulaID}", name="{self.name}", content="{self.content}")>'

class StudentStandard(Base):
    __tablename__ = "StudentStandard"

    studentStandardID = Column(Integer, primary_key=True, autoincrement=True)
    studentID = Column(Integer)
    standardID = Column(Integer)
    grade = Column(String)

    def __init__(self, studentStandardID, studentID, standardID, grade):
        self.studentStandardID = studentStandardID
        self.studentID = studentID
        self.standardID = standardID
        self.grade = grade

    def __repr__(self):
        return f'<StudentStandard (studentStandardID="{self.studentStandardID}", studentID="{self.studentID}", standardID="{self.standardID}", grade="{self.grade}")>'

class Shape(Base):
    __tablename__ = "Shape"

    shapeID = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String)   
    SVG = Column(String)

    def __init__(self, shapeID, type, SVG):
        self.shapeID = shapeID
        self.type = type
        self.SVG = SVG

    def __repr__(self):
        return f'<Shape (shapeID="{self.shapeID}", type="{self.type}", SVG="{self.SVG}")>'

class Student(Base):
    __tablename__ = "Student"

    studentID = Column(Integer, primary_key=True, autoincrement=True)
    fName= Column(String)
    lName= Column(String)
    courseID = Column(Integer)

    def __init__(self, studentID, fName, lName, courseID):
        self.studentID = studentID
        self.fName = fName
        self.lName = lName
        self.courseID = courseID

    def __repr__(self):
        return f'<Student (studentID="{self.studentID}", fName="{self.fName}", lName="{self.lName}", courseID="{self.courseID}")>'

class Variable(Base):
    __tablename__ = "Variable"

    variableID = Column(Integer, primary_key=True, autoincrement=True)
    questionID = Column(Integer)
    name = Column(String)
    detials = Column(String)

    def __init__(self, variableID, questionID, name, details):
        self.variableID = variableID
        self.questionID = questionID
        self.name = name
        self.details = details

    def __repr__(self):
        return f'<variableID (id="{self.variableID}", questionID="{self.questionID}", name="{self.name}", details="{self.details}")>'
