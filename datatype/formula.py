from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

base = declarative_base()

class Formula(base):
    __table_name__ = "Formula"

    formulaID = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    content = Column(String)

    def __init__(self, formulaID, name, content):
        self.formulaID = formulaID
        self.name = name
        self.content = content

    def __repr__(self):
        return f'<Formula (formulaID="{self.formulaID}", name="{self.name}", content="{self.content}")>'
