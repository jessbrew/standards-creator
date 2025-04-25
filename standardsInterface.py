from datatypes import Standard
from database import Database

db = Database("sqlite:///standards_creator.db")
db.connect()

db_standards = db.get_all_standards()
standards_list = []

for s in db_standards:
    standards_list.append(Standard(s.name, s.standardNumber,s.courseID))

def getAllStandards():
    return standards_list

