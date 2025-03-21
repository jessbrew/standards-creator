CREATE TABLE Course (
    courseID INTEGER PRIMARY KEY,
    name TEXT,
    semester TEXT,
    courseCode TEXT
);

CREATE TABLE Standard (
    standardID INTEGER PRIMARY KEY,
    standardNumber INTEGER,
    name TEXT,
    courseID INTEGER,
    FOREIGN KEY (courseID) REFERENCES Course(courseID)
);

CREATE TABLE Student (
    studentID INTEGER PRIMARY KEY,
    fName TEXT,
    lName TEXT,
    courseID INTEGER,
    FOREIGN KEY (courseID) REFERENCES Course(courseID)
);

CREATE TABLE StudentStandard (
    studentStandardID INTEGER PRIMARY KEY,
    studentID INTEGER,
    standardID INTEGER,
    grade TEXT,
    FOREIGN KEY (studentID) REFERENCES Student(studentID),
    FOREIGN KEY (standardID) REFERENCES Standard(standardID)
);

CREATE TABLE Problem (
    problemID INTEGER PRIMARY KEY,
    content TEXT,
    standardID INTEGER,
    FOREIGN KEY (standardID) REFERENCES Standard(standardID)
);

CREATE TABLE Formula (
    formulaID INTEGER PRIMARY KEY,
    name TEXT,
    content TEXT
);

CREATE TABLE Variable (
    variableID INTEGER PRIMARY KEY,
    problemID INTEGER,
    name TEXT,
    details TEXT,
    FOREIGN KEY (problemID) REFERENCES Problem(problemID)
);

CREATE TABLE Shape (
    shapeID INTEGER PRIMARY KEY,
    type TEXT,
    SVG TEXT
);
