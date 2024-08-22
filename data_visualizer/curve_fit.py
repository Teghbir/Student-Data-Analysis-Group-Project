# ECOR 1042 Lab 6 - Individual submission for curve_fit function

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Teghbir Chadha"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101258511"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T99"

#==========================================#
# Place your curve_fit function after this line
import numpy as np


def curve_fit(data: list[dict], attribute: str, degree: int) -> str:
    """Return a string representation of the equation of the best fit for the average of
    G_Avg (e.g. “y = 3x^2+x+1”)
    >>> curve_fit([{"Failures": 18, "Absences": 3, "G_Avg": 5.67}, {"Failures": 17, "Absences": 3, "G_Avg": 3.67}, {"Failures": 16, "Absences": 3, "G_Avg": 1.56}], "Failures", 2)
    y = -0.06x^2 + 3.93x + -47.16
    >>>curve_fit([{"Age": 10, "Absences": 3, "G_Avg": 9.67}, {"Age": 17, "Absences": 3, "G_Avg": 3.67}, {"Age": 16, "Absences": 3, "G_Avg": 1.56}, {"Age": 4, "Absences": 3, "G_Avg": 1.56}], "Age", 2 )
    y = -0.02x^3 + 0.74x^2 + -9.52x + 28.84
    >>>curve_fit([{"Age": 18, "Absences": 3, "G_Avg": 15.67}, {"Age": 17, "Absences": 3, "G_Avg": 3.67}], "Age", 4 )
    y = 2.0x + -30.33
    """
    x_data = []
    for student in data:
        if student[attribute] not in x_data:
            x_data.append(student[attribute])

    G_Avg_values = []
    for student in data:
        G_Avg_values.append((student[attribute], student['G_Avg']))

    y_data = []

    for x in x_data:
        total = 0
        for g in G_Avg_values:
            if g[0] == x:
                total += g[1]
        y_data.append(total)

    if len(x_data) < degree:
        value = np.polyfit(x_data, y_data, len(x_data) - 1)
        degree = len(x_data) - 1
    else:
        value = np.polyfit(x_data, y_data, degree)

    if degree == 1:
        x = str(value[0]) + "x"
        c = str(value[1])
        eqn_str = "y = " + x + " + " + c
        return eqn_str
    elif degree == 2:
        x1 = str(value[0]) + "x^2"
        x2 = str(value[1]) + "x"
        c = str(value[2])
        eqn_str = "y = " + x1 + " + " + x2 + " + " + c
        return eqn_str
    elif degree == 3:
        x1 = str(value[0]) + "x^3"
        x2 = str(value[1]) + "x^2"
        x3 = str(value[2]) + "x"
        c = str(value[3])
        eqn_str = "y = " + x1 + " + " + x2 + " + " + x3 + " + " + c
        return eqn_str
    elif degree == 4:
        x1 = str(value[0]) + "x^4"
        x2 = str(value[1]) + "x^3"
        x3 = str(value[2]) + "x^2"
        x4 = str(value[3]) + "x"
        c = str(value[4])
        eqn_str = "y = " + x1 + " + " + x2 + " + " + x3 + " + " + x4 + " + " + c
        return eqn_str
    elif degree == 5:
        x1 = str(value[0]) + "x^5"
        x2 = str(value[1]) + "x^4"
        x3 = str(value[2]) + "x^3"
        x4 = str(value[3]) + "x^2"
        x5 = str(value[4]) + "x"
        c = str(value[5])
        eqn_str = "y = " + x1 + " + " + x2 + " + " + \
            x3 + " + " + x4 + " + " + x5 + " + " + c
        return eqn_str


# Do NOT include a main script in your submission