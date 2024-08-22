# ECOR 1042 Lab 6 - Individual submission for histogram

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Yahia Omeman"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101266616"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-99"

#==========================================#
# Place your histogram function after this line
import matplotlib.pyplot as plt

def histogram(list_of_dict: list[dict], attribute_of_plot: str):
    """The function will take two input parameters, the first is a list of dictionaries, and the second is a string. The string will indicate what attribute will be
    plotted. The function will go through all students and store the number of students that are at each level of the attribute and return the histogram.
    >>> histogram([{"Age": 18, "Absences": 3, "G_Avg": 5.67}, {"Age": 17, "Absences": 3, "G_Avg": 5.67}, {"Age": 18, "Absences": 3, "G_Avg": 1.56}], "Age")
    displays a histogram
    >>>histogram([{"Gender": "Male", "Age": 9, "GPA": 3.2}, {"Gender": "Female", "Age": 20, "GPA": 3.5}, {"Gender": "Male", "Age": 19, "GPA": 2.9}], "GPA")
    displays a histogram
    >>>histogram([{"Subject": "Math", "Score": 70}, {"Subject": "Science", "Score": 85}, {"Subject": "English", "Score": 80}], "Score")displays a histogram
    histogram([{"Age": 18, "Absences": 3, "G_Avg": 5.67}, {"Age": 17, "Absences": 3, "G_Avg": 5.67}, {"Age": 18, "Absences": 3, "G_Avg": 1.56}], "Age")
    """
    
    count_dict = {}

    for dictionary in list_of_dict:
        if attribute_of_plot in dictionary:
            value = dictionary[attribute_of_plot]
            if type(value) == int or type(value) == float:
                value = int(round(value))
            count_dict[value] = count_dict.get(value, 0) + 1

    max_count = max(count_dict.values())
    attribute_values = sorted(list(count_dict.keys()))
    
    counts = []
    for value in attribute_values:
        counts.append(count_dict[value])

    plt.xlabel(attribute_of_plot)
    plt.ylabel("Number of Students")
    plt.xlim(min(attribute_values), max(attribute_values))
    plt.ylim(0, max_count + 1)
    plt.bar(attribute_values, counts, 0.5)
    plt.show()
    
    return None

# Do NOT include a main script in your submission