from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base

engine = create_engine("sqlite://")
base = declarative_base()

class Variable(base):
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