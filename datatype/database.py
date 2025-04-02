from sqlalchemy import create_engine, column, Integer, String, Column
from sqlalchemy.orm import sessionmaker, declarative_base
# Create the base class to map a class to the table
Base = declarative_base()

from variable import Variable
from standard import Standard

class Database:
    def __init__(self, db_url):
        self.db_url = db_url
        self.engine = None
        self.Session = None

    def connect(self):
        """Connects to the sqlite3 database"""
        self.engine = create_engine(self.db_url, echo=False)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        return self.engine

    def disconnect(self):
        if self.engine is not None:
            self.engine.dispose()

    def connection_check(self):
        """Get all dinos from the dion_info table"""
        session = self.Session()
        print("Connected to database")
        session.close()

    # def build_standard(self):





if __name__ == '__main__':
    # create db connection
    db = Database("sqlite:///standards_creator.db")

    db.connect()
    db.connection_check()
    db.disconnect()

