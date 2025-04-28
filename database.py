from sqlalchemy import create_engine, Integer, String, Column
from sqlalchemy.orm import sessionmaker, declarative_base

# Create the base class to map classes to database tables
Base = declarative_base()

from datatypes import Standard, Part, Question, Course, Formula, StudentStandard, Shape, Student, Variable

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
    
    ################################
    # CRUD Operations for Standard #
    ################################

    def create_standard(self, name, number, courseID):
        session = self.Session()
        standard = Standard(name=name, number=number, courseID=courseID)
        session.add(standard)
        session.commit()
        session.close()
        return standard

    def get_standard(self, standard_id):
        session = self.Session()
        standard = session.query(Standard).filter_by(standardID=standard_id).first()
        session.close()
        return standard

    def get_all_standards(self):
        """Fetches all standards from the database."""
        session = self.Session()
        standards = session.query(Standard).all()
        session.close()
        return standards

    def update_standard(self, standard_id, **kwargs):
        session = self.Session()
        standard = self.get_standard(standard_id)
        for key, value in kwargs.items():
            setattr(standard, key, value)
        session.commit()
        session.close()
        return standard

    def delete_standard(self, standard_id):
        session = self.Session()
        standard = self.get_standard(session, standard_id)
        if standard:
            session.delete(standard)
            session.commit()
            session.close()

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
    
    def insert_standard(self, standard):
        self.create_standard(standard.name, standard.number, standard.courseID)
        for question in standard.questions:
            self.create_question(question.content, question.standardID)
            for part in question.parts:
                self.create_part(part.content, part.questionID)
        

    
    #################################
    # CRUD Operations for Questions #
    #################################

    def create_question(self, content, standardID):
        session = self.Session()
        question = Question(content=content, standardID=standardID)
        session.add(question)
        session.commit()
        return question

    def get_question(self, question_id):
        session = self.Session()
        question = session.query(Question).filter_by(questionID=question_id).first()
        session.close()
        return question
    
    def get_all_questions(self):
        """Fetches all questions from the database."""
        session = self.Session()
        questions = session.query(Question).all()
        session.close()
        return questions

    def update_question(self, question_id, **kwargs):
        session = self.Session()
        question = self.get_question(question_id)
        for key, value in kwargs.items():
            setattr(question, key, value)
        session.commit()
        session.close()
        return question

    def delete_question(self, question_id):
        session = self.Session()
        question = self.get_question( question_id)
        if question:
            session.delete(question)
            session.commit()

    ############################
    # CRUD Operations for Part #
    ############################

    def create_part(self, content, questionID):
        session = self.Session()
        part = Part(content=content, questionID=questionID)
        session.add(part)
        session.commit()
        session.close()
        return part

    def get_part(self, part_id):
        session = self.Session()
        part = session.query(Part).filter_by(partID=part_id).first()
        session.close()
        return part
    
    def get_all_parts(self):
        """Fetches all parts from the database."""
        session = self.Session()
        parts = session.query(Part).all()
        session.close()
        return parts

    def update_part(self, part_id, **kwargs):
        session = self.Session()
        part = self.get_part(part_id)
        for key, value in kwargs.items():
            setattr(part, key, value)
        session.commit()
        session.close()
        return part

    def delete_part(self, part_id):
        session = self.Session()
        part = self.get_part(part_id)
        if part:
            session.delete(part)
            session.commit()
            session.close()

    ##############################
    # CRUD Operations for Course #
    ##############################

    def create_course(self, name, semester, courseCode):
        session = self.Session()
        course = Course(courseID=None, name=name, semester=semester, courseCode=courseCode)
        session.add(course)
        session.commit()
        session.close()
        return course

    def get_course(self, course_id):
        session = self.Session()
        course = session.query(Course).filter_by(courseID=course_id).first()
        session.close()
        return course

    def update_course(self, course_id, **kwargs):
        session = self.Session()
        course = self.get_course(course_id)
        for key, value in kwargs.items():
            setattr(course, key, value)
        session.commit()
        session.close()
        return course

    def delete_course(self, course_id):
        session = self.Session()
        course = self.get_course(course_id)
        if course:
            session.delete(course)
            session.commit()
            session.close()

    ###############################
    # CRUD Operations for Formula #
    ###############################

    def create_formula(self, name, content):
        session = self.Session()
        formula = Formula(formulaID=None, name=name, content=content)
        session.add(formula)
        session.commit()
        session.close
        return formula

    def get_formula(self, formula_id):
        session = self.Session()
        formula = session.query(Formula).filter_by(formulaID=formula_id).first()
        session.close()
        return formula

    def update_formula(self, formula_id, **kwargs):
        session = self.Session()
        formula = self.get_formula(formula_id)
        for key, value in kwargs.items():
            setattr(formula, key, value)
        session.commit()
        session.close()
        return formula

    def delete_formula(self, formula_id):
        session = self.Session()
        formula = self.get_formula(formula_id)
        if formula:
            session.delete(formula)
            session.commit()
            session.close()

    #######################################
    # CRUD Operations for StudentStandard #
    #######################################

    def create_student_standard(self, studentID, standardID, grade):
        session = self.Session()
        ss = StudentStandard(studentStandardID=None, studentID=studentID, standardID=standardID, grade=grade)
        session.add(ss)
        session.commit()
        session.close()
        return ss

    def get_student_standard(self, student_standard_id):
        session = self.Session()
        ss = session.query(StudentStandard).filter_by(studentStandardID=student_standard_id).first()
        session.close()
        return ss

    def update_student_standard(self, student_standard_id, **kwargs):
        session = self.Session()
        ss = self.get_student_standard(self, student_standard_id)
        for key, value in kwargs.items():
            setattr(ss, key, value)
        session.commit()
        session.close()
        return ss

    def delete_student_standard(self, student_standard_id):
        session = self.Session()
        ss = self.get_student_standard(student_standard_id)
        if ss:
            session.delete(ss)
            session.commit()
            session.close()

    #############################
    # CRUD Operations for Shape #
    #############################

    def create_shape(self, type, SVG):
        session = self.Session()
        shape = Shape(shapeID=None, type=type, SVG=SVG)
        session.add(shape)
        session.commit()
        session.close()
        return shape

    def get_shape(self, shape_id):
        session = self.Session()
        shape = session.query(Shape).filter_by(shapeID=shape_id).first()
        session.close()
        return shape

    def update_shape(self, shape_id, **kwargs):
        session = self.Session()
        shape = self.get_shape(shape_id)
        for key, value in kwargs.items():
            setattr(shape, key, value)
        session.commit()
        session.close()
        return shape

    def delete_shape(self, shape_id):
        session = self.Session()
        shape = self.get_shape(shape_id)
        if shape:
            session.delete(shape)
            session.commit()
        session.close()

    #CRUD Operations for Student
    def create_student(self, fName, lName, courseID):
        session = self.Session()
        student = Student(studentID=None, fName=fName, lName=lName, courseID=courseID)
        session.add(student)
        session.commit()
        session.close()
        return student

    def get_student(self, student_id):
        session = self.Session()
        student = session.query(Student).filter_by(studentID=student_id).first()
        session.close()
        return student

    def update_student(self, student_id, **kwargs):
        session = self.Session()
        student = self.get_student(student_id)
        for key, value in kwargs.items():
            setattr(student, key, value)
        session.commit()
        session.close()
        return student

    def delete_student(self, student_id):
        session = self.Session()
        student = self.get_student(student_id)
        if student:
            session.delete(student)
            session.commit()
        session.close()

    #CRUD Operations for Variable
    def create_variable(self, questionID, name, details):
        session = self.Session()
        variable = Variable(variableID=None, questionID=questionID, name=name, details=details)
        session.add(variable)
        session.commit()
        session.close()
        return variable

    def get_variable(self, variable_id):
        session = self.Session()
        variable = session.query(Variable).filter_by(variableID=variable_id).first()
        session.close()
        return variable

    def update_variable(self, variable_id, **kwargs):
        session = self.Session()
        variable = self.get_variable(variable_id)
        for key, value in kwargs.items():
            setattr(variable, key, value)
        session.commit()
        session.close()
        return variable

    def delete_variable(self, variable_id):
        session = self.Session()
        variable = self.get_variable(variable_id)
        if variable:
            session.delete(variable)
            session.commit()
        session.close()

    def make_standard(self, idNum):
        session = self.Session()
        standard = session.query(Standard).filter(Standard.standardID == idNum).first()
        standardQuestions = []
        questionParts = []
        for question in standard.questions:
            standardQuestions.append(question)
            for part in question.parts:
                questionParts.append(part.content)
        return(standard, standardQuestions, questionParts)

    def make_test(self, idNumList):
        session = self.Session()
        standards = []
        for idNum in idNumList:
            standard = self.create_standard(idNum)
            standards.append(standard)
        return standards

    def print_test(self, test):
        session = self.Session()
        for test in test:
            standard, standardQuestions, questionParts = test
            print(standard.name)
            for question in standardQuestions:
                print(' ' + question.content)
                for part in questionParts:
                    print('     ' + part)
            print('\n')





    




if __name__ == "__main__":
    # Create a database connection
    db = Database("sqlite:///standards_creator.db")
    db.connect()
    db.connection_check()
    db.disconnect()
