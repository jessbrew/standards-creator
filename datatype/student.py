from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

base = declarative_base()

class Student(base):
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
