from sqlalchemy import create_engine, Integer, String, Column
from sqlalchemy.orm import sessionmaker, declarative_base

# Create the base class to map classes to database tables
Base = declarative_base()

from variable import Variable
from standard import Standard
from question import Question
from part import Part


class Database:
    def __init__(self, db_url):
        self.db_url = db_url
        self.engine = None
        self.Session = None

    def connect(self):
        """Connects to the SQLite database and creates tables if they don't exist."""
        self.engine = create_engine(self.db_url, echo=False)
        Base.metadata.create_all(self.engine)  # Ensure tables are created
        self.Session = sessionmaker(bind=self.engine)
        return self.engine

    def disconnect(self):
        """Disconnects from the database."""
        if self.engine is not None:
            self.engine.dispose()

    def connection_check(self):
        """Checks if the database connection is working."""
        session = self.Session()
        print("Connected to database")
        session.close()

    def get_all_standards(self):
        """Fetches all standards from the database."""
        session = self.Session()
        standards = session.query(Standard).all()
        session.close()
        return standards

    def get_all_questions(self):
        """Fetches all questions from the database."""
        session = self.Session()
        questions = session.query(Question).all()
        session.close()
        return questions

    def get_all_parts(self):
        """Fetches all parts from the database."""
        session = self.Session()
        parts = session.query(Part).all()
        session.close()
        return parts

if __name__ == "__main__":
    # Create a database connection
    db = Database("sqlite:///standards_creator.db")

    db.connect()
    db.connection_check()

    # Fetch and print some sample data
    print("Standards:", db.get_all_standards())
    # print("Questions:", db.get_all_questions())
    # print("Parts:", db.get_all_parts())

    db.disconnect()