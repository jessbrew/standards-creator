from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

base = declarative_base()

class StudentStandard(base):
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
