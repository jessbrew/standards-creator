from datatype.standard import Standard
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
standards.append(Standard(1, "Trig", 3,1))
standards.append(Standard(2, "Trig", 3,1))
standards.append(Standard(2, "Geo", 1,1))
standards.append(Standard(1, "Angles", 2,1))
standards.append(Standard(1, "Unit Circles", 4,1))
standards.append(Standard(2, "Unit Circles", 4,1))
standards.append(Standard(1, "Vectors", 5,1))
standards.append(Standard(2, "Vectors", 5,1))
standards.append(Standard(1, "Cosines", 6,1))
standards.append(Standard(2, "Cosines", 6,1))
standards.append(Standard(1, "Graphs", 7,1))
standards.append(Standard(1, "Triangles", 8,1))
standards.append(Standard(1, "Sines", 9,1))
standards.append(Standard(1, "Functions", 10,1))

def getAllStandards():
    return standards