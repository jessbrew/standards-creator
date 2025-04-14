from datatypes import Standard
# from datatype.database import Database


# db = Database("sqlite:///standards_creator.db")
# db.connect()
#
# standards = db.get_all_standards()
# for s in standards:
#     print(s.name)


standards = []
# id = version num
# name == name
# number = standard number
standards.append(Standard("Trig", 3,1))
standards.append(Standard("Trig", 3,1))
standards.append(Standard( "Geo", 1,1))
standards.append(Standard("Angles", 2,1))
standards.append(Standard("Unit Circles", 4,1))
standards.append(Standard( "Unit Circles", 4,1))
standards.append(Standard( "Vectors", 5,1))
standards.append(Standard("Vectors", 5,1))
standards.append(Standard( "Cosines", 6,1))
standards.append(Standard("Cosines", 6,1))
standards.append(Standard("Graphs", 7,1))
standards.append(Standard("Triangles", 8,1))
standards.append(Standard( "Sines", 9,1))
standards.append(Standard("Functions", 10,1))
#
def getAllStandards():
    return standards