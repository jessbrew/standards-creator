from datatype.standard import Standard
from collections import defaultdict

standards = []

standards.append(Standard("Trig: ", 1, 0))
standards.append(Standard("Geo: ", 2, 1))
standards.append(Standard("Angles: ", 3, 2))  # version 1
standards.append(Standard("Unit Circle: ", 3, 0))  # version 2
standards.append(Standard("Vectors: ", 4, 0))
standards.append(Standard("Cosines: ", 5, 0))  # version 1
standards.append(Standard("Graphs: ", 5, 0))  # version 2
standards.append(Standard("Triangles: ", 6, 0))  # version 1
standards.append(Standard("Sines: ", 6, 0))  # version 2
standards.append(Standard("Functions: ", 10, 0))    # standalone

def getAllStandards():
    return standards
