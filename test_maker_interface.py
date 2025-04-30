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
    # make sure 'standards' is a list, not a string
    if isinstance(standards, str):
        # remove commas & spaces
        standards = standards.replace(",", "")
        standards = standards.replace(" ", "")
        # make standards into array of INTS
        int_standards = []
        for standard in standards:
            int_standards.append(int(standard))
        standards = int_standards
        
    # make sure 'standards' is a list (not a single value)
    if not isinstance(standards, list):
        standards = [standards]

    # update dictionary
    students_dictionary.update({student_name : standards}) # name : standards