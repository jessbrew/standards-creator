from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

base = declarative_base()

class Shape(base):
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
