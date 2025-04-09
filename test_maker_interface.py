import sheets_api

def get_all_student_standards(spreadsheet_id):
    """
    Returns dictionary containing students & their chosen standards,
    grabbed from a Google sheet with given 'spreadsheet_id'
    """
    return sheets_api.get_student_standards(spreadsheet_id)


# temporarily appends another student & their standards to the dictionary
def add_student_standards(students_dictionary, student_name, standards):
    """
    Appends another 'student_name' & their 'standards' to 'students_dictionary'
    """
    # make sure 'standards' is a list, not a single number
    if not isinstance(standards, list): 
        standards = [standards]
    # update dictionary
    students_dictionary.update({student_name : standards}) # name : standards