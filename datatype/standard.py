from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

base = declarative_base()

class Standard(base):
    __table_name__ = "Standard"

    standardID = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    number = Column(Integer)
    courseID = Column(Integer)

    def __init__(self, standardID, name, number, courseID):
        self.name = name
        self.number = number
        self.standardID = standardID
        self.courseID = courseID

