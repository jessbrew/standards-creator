from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

base = declarative_base()

class Part(base):
    __tablename__ = "Part"

    partID = Column(Integer, primary_key=True, autoincrement=True)
    questionID = Column(Integer)
    content = Column(String)

    def __init__(self, partID, questionID, content):
        self.partID = partID
        self.questionID = questionID
        self.content = content

    def __repr__(self):
        return f'<Part (partID="{self.partID}", questionID="{self.questionID}", content="{self.content}")>'
