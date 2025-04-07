from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

base = declarative_base()

class Standard(base):
    __tablename__ = "Standard"

    standardID = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    standardNumber = Column(Integer)
    courseID = Column(Integer)

    def __init__(self, standardID, name, number, courseID):
        self.name = name
        self.standardNumber = number
        self.standardID = standardID
        self.courseID = courseID

    def __repr__(self):
        return f'<Standard (standardID="{self.standardID}", name="{self.name}", standardNumber="{self.standardNumber}", courseID="{self.courseID}")>'

