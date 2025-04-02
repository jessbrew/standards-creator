from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

base = declarative_base()

class Question(base):
    __table_name__ = "Question"

    questionID = Column(Integer, primary_key=True, autoincrement=True)
    standardID = Column(Integer)
    content = Column(String)

    def __init__(self, questionID, standardID, content):
        self.questionID = questionID
        self.standardID = standardID
        self.content = content

    def __repr__(self):
        return f'<Question (questionID="{self.questionID}", standardID="{self.standardID}", content="{self.content}")>'
