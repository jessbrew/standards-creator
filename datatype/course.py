from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

base = declarative_base()

class Course(base):
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
