# ECOR 1042 Lab 6 - Individual submission for batch_UI

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Michael Acquah"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101220886"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T99"

#==========================================#
# Place your script for your batch_UI after this line
import load_data
import sort
import histogram
import curve_fit


file = input("Please input the name of the file where your commands are stored: ")
infile = open(file, 'r')  
data = []

for line in infile:
    data.append((line.replace("\n", "").split(";")))

output = []
loaded = False

for data in data:
    input = data[0].upper()

    if input == "L":
        output = load_data.add_average(
            load_data.load_data(data[1], (data[2], data[3])))
        loaded = True
        print("Data was loaded.")

    elif input == "S":
        if loaded == False:
            print("File was not loaded. Please, load a file first.")
        else:
            output = sort.sort(output, data[2], data[1])

        if data[3].upper() == "Y":
            print(output)
            print("Data sorted.")
        else:
            print("Data sorted.")

    elif input == "C":
        # checks if the output is empty
        if loaded == False:
            print("File not loaded. Please, load a file first")
        else:
            print(curve_fit.curve_fit(output, data[1], int(data[2])))

    elif input == "H":
        # checks if the output is empty
        if loaded == False:
            print("File not loaded. Please, load a file first")
        else:
            histogram.histogram(output, data[1])

    elif input == "E":
        break


