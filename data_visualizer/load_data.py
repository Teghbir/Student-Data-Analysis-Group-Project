# ECOR 1042 Lab 3 - Team submission
# Remember to include docstring and type annotations for your functions


# Update "" to list all students contributing to the team work
__author__ = "Teghbir Chadha, Michael Acquah, Tyler Knox, Yahia Omeman"

# Update "" with your team (e.g. T102)
__team__ = "T99"

#==========================================#
# Place your student_school_list function after this line
def student_school_list(file_name: str, school_name: str) -> list:
    """Returns a list of students (stored as a dictionary) that attended the school and the keys of each dictionary are for all atributes except "School"
    Preconditions: none
    >>>student_school_list("student-mat.csv", "GP")
    [{'Age': 18, 'StudyTime': 2, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}, {another element}...]
    >>>student_school_list("student-mat.csv", "MS")
    [{'Age': 18, 'StudyTime': 2, 'Failures': 0, 'Health': 5, 'Absences': 2, 'G1': 11, 'G2': 11, 'G3': 11}, {another element}...]
    >>>student_school_list("student-mat.csv", "Pizza")
    []
    """
    infile = open(file_name, "r")
    student_list = []
    
    for line in infile:
        data_list = line.strip().split(",")
        if data_list[0] == school_name:
            dictionary = {}
            dictionary["Age"] = int(data_list[1])
            dictionary["StudyTime"] = int(data_list[2])
            dictionary["Failures"] = int(data_list[3])
            dictionary["Health"] = int(data_list[4])
            dictionary["Absences"] = int(data_list[5])
            dictionary["G1"] = int(data_list[6])
            dictionary["G2"] = int(data_list[7])
            dictionary["G3"] = int(data_list[8])
            student_list.append(dictionary)
        
    infile.close()
    return student_list

#==========================================#
# Place your student_health_list function after this line
def student_health_list(file_name: str, health: int) -> list[dict]: 
    """Returns a list of students (stored as a dictionary) whose health equals the provided value and the keys of each dictionary are for all atributes except "Health"
    Precondition: none
    >>>student_health_list('student-mat.csv', 2)
    [{'School': 'GP', 'Age': 15, 'StudyTime': 2, 'Failures': 0, 'Absences': 0, 'G1': 10, 'G2': 8, 'G3': 9}, {another element}]
    >>>student_health_list('student-mat.csv', 1)
    [{'School': 'GP', 'Age': 17, 'StudyTime': 2, 'Failures': 0, 'Absences': 6, 'G1': 6, 'G2': 5, 'G3': 6}, {another element}]
    >>>student_health_list('student-mat.csv', -3)
    []
    """
    infile = open(file_name, "r")
    student_list = [ ]    
    
    for line in infile:
        data_list = line.strip().split(",")
        if data_list[4] == str(health):
            dictionary = {}
            dictionary["School"] = str(data_list[0])            
            dictionary["Age"] = int(data_list[1])
            dictionary["StudyTime"] = int(data_list[2])
            dictionary["Failures"] = int(data_list[3])
            dictionary["Absences"] = int(data_list[5])
            dictionary["G1"] = int(data_list[6])
            dictionary["G2"] = int(data_list[7])
            dictionary["G3"] = int(data_list[8])
            student_list.append(dictionary)
        
    infile.close()
    return student_list    

#==========================================#
# Place your student_age_list function after this line
def student_age_list(file_name: str, age: int) -> list[dict]:
    """Returns a list of students (stored as a dictionary) whose age equals the specified value and the keys of each dictionary are for all atributes except "Age"
    Preconditions: none
    >>>student_age_list('student-mat.csv', 30)
    []
    >>>student_age_list('student-mat.csv', 20)
    [{'School': 'BD', 'StudyTime': 1, 'Failures': 0, 'Health': 5, 'Absences': 0, 'G1': 17, 'G2': 18, 'G3': 18}, {another element}]
    >>>student_age_list('student-mat.csv', 16)
    [{'School': 'GP', 'StudyTime': 2, 'Failures': 0, 'Health': 5, 'Absences': 4, 'G1': 6, 'G2': 10, 'G3': 10}, {another element}]
    """
    infile = open(file_name, "r")
    student_list = []
    
    for line in infile:
        data_list = line.strip().split(",")
        if data_list[1] == str(age):
            dictionary = {}
            dictionary["School"] = str(data_list[0])
            dictionary["StudyTime"] = int(data_list[2])
            dictionary["Failures"] = int(data_list[3])
            dictionary["Health"] = int(data_list[4])
            dictionary["Absences"] = int(data_list[5])
            dictionary["G1"] = int(data_list[6])
            dictionary["G2"] = int(data_list[7])
            dictionary["G3"] = int(data_list[8])
            student_list.append(dictionary)
        
    infile.close()
    return student_list

#==========================================#
# Place your student_failures_list function after this line
def student_failures_list(file_name: str, failures: int) ->  list[dict]:
    """Returns a list of students (stored as a dictionary) whose failures equal the specified value and the keys of each dictionary are for all atributes except "Failures"
    Preconditions: none
    >>>student_failures_list('student-mat.csv', 30)
    []
    >>>student_failures_list('student-mat.csv', 0)
    [{'School': 'GP', 'Age': 18, 'StudyTime': 2, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}, {another element}]
    >>>student_failures_list('student-mat.csv', 1)
    [{'School': 'GP', 'Age': 16, 'StudyTime': 2, 'Health': 3, 'Absences': 25, 'G1': 7, 'G2': 10, 'G3': 11}, {another element}]
    """
    infile = open(file_name, "r")
    student_list = []
    
    for line in infile:
        data_list = line.strip().split(",")
        if data_list[3] == str(failures):
            dictionary = {}
            dictionary["School"] = str(data_list[0])
            dictionary["Age"] = int(data_list[1])
            dictionary["StudyTime"] = int(data_list[2])
            dictionary["Health"] = int(data_list[4])
            dictionary["Absences"] = int(data_list[5])
            dictionary["G1"] = int(data_list[6])
            dictionary["G2"] = int(data_list[7])
            dictionary["G3"] = int(data_list[8])
            student_list.append(dictionary)
        
    infile.close()
    return student_list

#==========================================#
# Place your load_data function after this line
def load_data(file_name: str, argument: tuple) -> list[dict]:
    """Returns a list of students(stored as a dictionary) based on the second parameter of the function which is a tuple. The first value of the tuple is used to filter the data and the second one is the value of the attribute used to filter the students and if the first value of the tuple is "All", and all data will be loaded and the second one can be ignored.If the first value of the tuple is invalid, the function will print the error message "Invalid Value" and return an empty list.
    >>>load_data('student-mat.csv', ('Failures', 0))
    [{'School': 'GP', 'Age': 18, 'StudyTime': 2, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}, {another element}...]
    >>>load_data('student-mat.csv', ('Pizza', 0))
    Invalid Value
    []
    >>>load_data('student-mat.csv', ('All', 101))
    [{'School': 'GP', 'Age': 18, 'StudyTime': 2, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}, {another element}...]
    """
    
    infile = open(file_name, 'r')
    students_list = []
    
    i = 0
    for line in infile:
        data_list = line.strip().split(",")
        
        
        if argument[0] == 'School':
            if data_list[0] == str(argument[1]):
                dictionary = {}
                dictionary["Age"] = int(data_list[1])
                dictionary["StudyTime"] = int(data_list[2])
                dictionary["Failures"] = int(data_list[3])
                dictionary["Health"] = int(data_list[4])
                dictionary["Absences"] = int(data_list[5])
                dictionary["G1"] = int(data_list[6])
                dictionary["G2"] = int(data_list[7])
                dictionary["G3"] = int(data_list[8])
                students_list.append(dictionary)        

        elif argument[0] == 'Age':
            if data_list[1] == str(argument[1]):
                dictionary = {}
                dictionary["School"] = str(data_list[0])
                dictionary["StudyTime"] = int(data_list[2])
                dictionary["Failures"] = int(data_list[3])
                dictionary["Health"] = int(data_list[4])
                dictionary["Absences"] = int(data_list[5])
                dictionary["G1"] = int(data_list[6])
                dictionary["G2"] = int(data_list[7])
                dictionary["G3"] = int(data_list[8])
                students_list.append(dictionary)     
      
        elif argument[0] == 'Failures':
            if data_list[3] == str(argument[1]):
                dictionary = {}
                dictionary["School"] = str(data_list[0])
                dictionary["Age"] = int(data_list[1])
                dictionary["StudyTime"] = int(data_list[2])
                dictionary["Health"] = int(data_list[4])
                dictionary["Absences"] = int(data_list[5])
                dictionary["G1"] = int(data_list[6])
                dictionary["G2"] = int(data_list[7])
                dictionary["G3"] = int(data_list[8])
                students_list.append(dictionary)  
              

        elif argument[0] == 'Health':
            if data_list[4] == str(argument[1]):
                dictionary = {}
                dictionary["School"] = str(data_list[0])
                dictionary["Age"] = int(data_list[1])
                dictionary["StudyTime"] = int(data_list[2])
                dictionary["Failures"] = int(data_list[3])
                dictionary["Absences"] = int(data_list[5])
                dictionary["G1"] = int(data_list[6])
                dictionary["G2"] = int(data_list[7])
                dictionary["G3"] = int(data_list[8])
                students_list.append(dictionary)

        elif argument[0] == 'All':
            if i!=0:
                dictionary = {}
                dictionary["School"] = str(data_list[0])
                dictionary["Age"] = int(data_list[1])
                dictionary["StudyTime"] = int(data_list[2])
                dictionary["Failures"] = int(data_list[3])
                dictionary["Health"] = int(data_list[4])
                dictionary["Absences"] = int(data_list[5])
                dictionary["G1"] = int(data_list[6])
                dictionary["G2"] = int(data_list[7])
                dictionary["G3"] = int(data_list[8])
                students_list.append(dictionary)     
        else:
            print("Invalid Value")
            break
     
        i+=1   

    infile.close()
    return students_list

#==========================================#
# Place your add_average function after this line
def add_average(students_list: list[dict]) -> list[dict]:
    """Returns a list of student dictionaries updated  with the average grade given one input parameter of a list of student dictionaries
    Preconditions: none
    >>>add_average([{'School': 'GP', 'Age': 18, 'StudyTime': 2, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}])
    [{'School': 'GP', 'Age': 18, 'StudyTime': 2, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6, 'G_Avg': 5.666666666666667}]
    >>>add_average([{'School': 'MP', 'Age': 16, 'StudyTime': 1, 'Failures': 0, 'Health': 3, 'Absences': 4, 'G1': 0, 'G2': 0, 'G3': 0}])
    [{'School': 'MP', 'Age': 16, 'StudyTime': 1, 'Failures': 0, 'Health': 3, 'Absences': 4, 'G1': 0, 'G2': 0, 'G3': 0, 'G_Avg': 0}]
    >>>add_average([{'School': 'GP', 'Age': 18, 'StudyTime': 2, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}, {'School': 'GP', 'Age': 17, 'StudyTime': 2, 'Health': 3, 'Absences': 4, 'G1': 5, 'G2': 5, 'G3': 6}])
    [{'School': 'GP', 'Age': 18, 'StudyTime': 2, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6, 'G_Avg': 5.666666666666667}, {'School': 'GP', 'Age': 17, 'StudyTime': 2, 'Health': 3, 'Absences': 4, 'G1': 5, 'G2': 5, 'G3': 6, 'G_Avg': 5.333333333333333}]
    """
    new_list = []
    for i in range(len(students_list)):
        new_dictionary = {}
        new_dictionary = students_list[i]
        g1 = new_dictionary['G1']
        g2 = new_dictionary['G2']
        g3 = new_dictionary['G3']
        avg = round((g1 + g2 + g3) / 3, 2)
        new_dictionary['G_Avg'] = avg
        new_list.append(new_dictionary)
    return new_list

# Do NOT include a main script in your submission



