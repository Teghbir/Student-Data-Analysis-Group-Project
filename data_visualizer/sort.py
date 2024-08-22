# ECOR 1042 Lab 5 - Team submission
# Remember to include docstring and type annotations for your functions

# Update "" to list all students contributing to the team work
__author__ = "Teghbir Chadha, Michael Acquah, Tyler Knox, Yahia Omeman"

# Update "" with your team (e.g. T102)
__team__ = "T99"

#==========================================#
# Place your sort_students_age_bubble function after this line
def sort_students_age_bubble(students_list: list[dict], sort_order: str) -> list[dict]:
    """Returns a sorted list from an unsorted list if the key "Age" is present in the dictionary; if "Age" is not present, then a message is outputted saying the key is not in the dictionary and the original list is returned
    >>>sort_students_age_bubble([{"Age":10,"School":"GP"},{"Age":19,"School":"MS"}], "D")
    [{'Age': 19, 'School': 'MS'}, {'Age': 10, 'School': 'GP'}]
    >>>sort_students_age_bubble([{"School":"GP"}, {"School":"MS"}], "D")
    "Age" key is not present.
    [{"School":"GP"}, {"School":"MS"}]
    >>>sort_students_age_bubble([{"Age":10,"School":"GP"},{"Age":19,"School":"MS"}], "A")
    [{'Age': 10, 'School': 'GP'}, {'Age': 19, 'School': 'MS'}]
    """
    index_length = len(students_list) - 1
    sorted = False
    
    if 'Age' in students_list[0]:
        existence = True
        while not sorted:
            sorted = True
            for i in range(0, index_length):
                if sort_order == 'A':
                    if students_list[i]['Age'] > students_list[i+1]['Age']:
                        sorted = False
                        students_list[i], students_list[i+1] = students_list[i+1], students_list[i]
                elif sort_order == 'D':
                    if students_list[i]['Age'] < students_list[i+1]['Age']:
                        sorted = False
                        students_list[i], students_list[i+1] = students_list[i+1], students_list[i]                
        return students_list
    else:
        print('"Age" key is not present')
        return students_list
    
#==========================================#
# Place your sort_students_time_selection function after this line
def sort_students_time_selection(students_list: list[dict], sort_order: str) -> list[dict]:
    """ Returns a list of dictionaries sorted either in ascending or descending sort_order based on the value of the StudyTime key and the inputted parameter 'A' or 'D'. If the key is not in the dictonary, a message is printed and the original list is returned. 
    >>> sort_students_time_selection ( [{"StudyTime":10.2,"School":"GP"},
    {"StudyTime":19.1,"School":"MS"}], "D")
    [{"StudyTime": 19.1, "School":"MS"}, {"StudyTime":10.2, "School":"GP"}]
    >>> sort_students_time_selection([{"School":"GP"},{"School":"MS"}], "D")
    "StudyTime" key is not present
    [{"School":"GP"}, {"School":"MS"}]
    >>> sort_students_time_selection ( [{"StudyTime":13,"School":"PG"}, {"StudyTime":21,"School":"MS"}], "A")
    [{'StudyTime': 13, 'School': 'PG'}, {'StudyTime': 21, 'School': 'MS'}]
    """
    keys = students_list[0].keys()
    studyTimeTrue = False
    for key in keys:
        if key == 'StudyTime':
            studyTimeTrue = True
            break

    if studyTimeTrue:
        if sort_order == 'D':
            for i in range(len(students_list)):
                min_idx = i
                for j in range(i + 1, len(students_list)):
                    if students_list[min_idx]['StudyTime'] < students_list[j]['StudyTime']:
                        min_idx = j
                students_list[i], students_list[min_idx] = students_list[min_idx], students_list[i]
        elif sort_order == 'A':
            for i in range(len(students_list)):
                min_idx = i
                for j in range(i + 1, len(students_list)):
                    if students_list[min_idx]['StudyTime'] > students_list[j]['StudyTime']:
                        min_idx = j
                students_list[i], students_list[min_idx] = students_list[min_idx], students_list[i]
    else:
        print(' "StudyTime" key is not present')

    return students_list

#==========================================#
# Place your sort_students_g_avg_insertion function after this line
def sort_students_g_avg_insertion(students_list: list[dict], sort_order: str) -> list[dict]:
    """Return a sorted list of students' grade averages in decending or ascending sort_order if the G_Avg section is present in the dictionary.
    >>> sort_students_g_avg_insertion( [{"G_Avg":7.2,"School":"GP"}, {"G_Avg":9.1,"School":"MS"}], "D")
    [{"G_Avg": 9.1, "School":"MS"}, {"G_Avg":7.2, "School":"GP"}]
    >>>sort_students_g_avg_insertion([{"School":"GP"},{"School":"MS"}], "D")
    "G_Avg" key is not present
    [{"School":"GP"}, {"School":"MS"}]
    >>>sort_students_g_avg_insertion( [{"G_Avg":7.2,"School":"GP"}, {"G_Avg":9.1,"School":"MS"}], "A")
    [{'G_Avg': 7.2, 'School': 'GP'}, {'G_Avg': 9.1, 'School': 'MS'}]
    """
    for key in students_list:
        if 'G_Avg' in key:
            condition = True
        else:
            condition = False
    if condition == True:
        if sort_order == 'D':
            for i in range(1, len(students_list)):
                key = students_list[i]
                j = i - 1
                while j >= 0 and key['G_Avg'] > students_list[j]['G_Avg']:
                    students_list[j + 1] = students_list[j]
                    j -= 1
                students_list[j + 1] = key
            return students_list
        elif sort_order == 'A':
            for i in range(1, len(students_list)):
                key = students_list[i]
                j = i - 1
                while j >= 0 and key['G_Avg'] < students_list[j]['G_Avg']:
                    students_list[j + 1] = students_list[j]
                    j -= 1
                students_list[j + 1] = key
            return students_list
    else:
        print('"G_Avg" key is not present')
        return students_list

#==========================================#
# Place your sort_students_failures_bubble function after this line
def sort_students_failures_bubble(students_list: list[dict], sort_order: str) -> list[dict]:
    """Returns a sorted list from an unsorted list if the key "Failures" is present in the dictionary; if "Failures" is not present, then a message is outputted saying the key is not in the dictionary and the original list is returned
    >>>sort_students_failures_bubble([{"Failures":10,"School":"GP"},{"Failures":19,"School":"MS"}], "D")
    [{"Failures": 19, "School":"MS"}, {"Failures":10, "School":"GP"}]
    >>>sort_students_failures_bubble([{"School":"GP"}, {"School":"MS"}], "D")
    "Failures" key is not present.
    [{"School":"GP"}, {"School":"MS"}]
    >>>sort_students_failures_bubble([{"Failures":10,"School":"GP"},{"Failures":19,"School":"MS"}], "D")
    [{'Failures': 19, 'School': 'MS'}, {'Failures': 10, 'School': 'GP'}]
    """
    index_length = len(students_list) - 1
    sorted = False
    
    if 'Failures' in students_list[0]:
        existence = True
        while not sorted:
            sorted = True
            for i in range(0, index_length):
                if sort_order == 'A':
                    if students_list[i]['Failures'] > students_list[i+1]['Failures']:
                        sorted = False
                        students_list[i], students_list[i+1] = students_list[i+1], students_list[i]
                elif sort_order == 'D':
                    if students_list[i]['Failures'] < students_list[i+1]['Failures']:
                        sorted = False
                        students_list[i], students_list[i+1] = students_list[i+1], students_list[i]                
        return students_list
    else:
        print('"Failures" key is not present')
        return students_list

#==========================================#
# Place your sort function after this line
def sort(students_list: list[dict], sort_order: str, value: str) -> list[dict]:
    """ It takes three input parameters: (1) a list of dictionaries, (2) a string (“A” or “D”) to determine if the students will be sorted in ascending or descending order, and (3) a string (“Age”, “StudyTime”, “G_Avg”, “Failures”) to determine the attribute used for sorting 
    >>>sort([{"Age":10,"School":"GP"},{"Age":19.1,"School":"MS"}],"D","Age")
    [{'Age': 19.1, 'School': 'MS'}, {'Age': 10, 'School': 'GP'}]
    >>>sort([{"School":"GP"},{"School":"MS"}], "D", "School")
   Cannot be sorted by "School"
   [{"School":"GP"}, {"School":"MS"}]
    >>>sort( [{"G_Avg":7.2,"School":"GP"}, {"G_Avg":4.3,"School":"AB"} ,{"G_Avg":9.1,"School":"MS"}], "A", "G_Avg")
    [{'G_Avg': 4.3, 'School': 'AB'}, {'G_Avg': 7.2, 'School': 'GP'}, {'G_Avg': 9.1, 'School': 'MS'}]
    """    
    if value == "Age":
        return sort_students_age_bubble(students_list, sort_order)
    elif value == "Failures":
        return sort_students_failures_bubble(students_list, sort_order)
    elif value == "StudyTime":
        return sort_students_time_selection(students_list, sort_order)
    elif value == "G_Avg":
        return sort_students_g_avg_insertion(students_list, sort_order)    
    else:
        print("Cannot be sorted by " + value)
        return students_list

# Do NOT include a main script in your submission


