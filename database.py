from sqlalchemy import create_engine, Integer, String, Column
from sqlalchemy.orm import sessionmaker, declarative_base

# Create the base class to map classes to database tables
Base = declarative_base()

from variable import Variable
from datatypes import Standard, Part, Question

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

    def create_standard(self, idNum):
        session = self.Session()
        standard = session.query(Standard).filter(Standard.standardID == idNum).first()
        standardQuestions = []
        questionParts = []
        for question in standard.questions:
            standardQuestions.append(question)
            for part in question.parts:
                questionParts.append(part.content)
        return(standard, standardQuestions, questionParts)
    
    def add_standard(self, standard, questions, parts, variables):
        session = self.Session()
        self.add_standard(standard)
        session.flush()
        for question in questions:   
            self.add_question(question)
        for part in parts:
            self.add_part(part)
        for variable in variables:
            self.add_variable(variable)


    def add_standard(self, standard):
        session = self.Session()
        session.add(standard)
        session.commit()

        session.refresh(standard)

        return standard
    
    def add_question(self, question):
        session = self.Session()
        session.add(question)
        session.commit()

        session.refresh(question)

        return question
    
    def add_part(self, part):
        session = self.Session()
        session.add(part)
        session.commit()

        session.refresh(part)

        return part
    
    def add_variable(self, variable):
        session = self.Session()
        session.add(variable)
        session.commit()

        session.refresh(variable)

        return variable




if __name__ == "__main__":
    # Create a database connection
    db = Database("sqlite:///standards_creator.db")
    db.connect()
    db.connection_check()

    # Fetch and print some sample data
    # For Standards
    # standards = db.get_all_standards()
    # print("Standards:")
    # for standard in standards:
    #     print(standard.name)

    # # For Questions
    # questions = db.get_all_questions()
    # print("Questions:")
    # for question in questions:
    #     print(question.content)

    # # For Parts
    # parts = db.get_all_parts()
    # print("Parts:")
    # for part in parts:
    #     print(part.content)
    standard_one, standard_one_q, standard_one_p = db.create_standard(1)
    print(standard_one)
    print(standard_one_q)
    print(standard_one_p)



    db.disconnect()
