# ECOR 1042 Lab 6 - Individual submission for text_UI

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Tyler Knox"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101270968"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T99"

#==========================================#
# Place your script for your text_UI after this line
import load_data as ld
import sort
import histogram as hst
import curve_fit as cf


data1 = []
attr1 = ''
condition = True
while condition == True:
    print('The available commands are:\n    L)oad Data\n    S)ort Data\n    C)urve Fit\n    H)istogram\n    E)xit\n')
    input1 = input('Please type your command: ')
    if input1 == 'L' or input1 == 'l':
        file1 = input('Please enter the name of the file: ')
        attr1 = input('Please enter the attribute to use as a filter: ')
        while attr1 != 'All' and attr1 != 'School' and attr1 != 'Age' and attr1 != 'Health' and attr1 != 'Failures':
            print('Invalid command. Try again')
            attr1 = input('Please enter the attribute to use as a filter: ')
        if attr1 == 'All':
            data1 = ld.add_average(ld.load_data(file1, (attr1, 1)))
        else:
            if attr1 == 'School':
                valu1 = input('Please enter the value of the attribute: ')
            else:
                valu1 = int(input('Please enter the value of the attribute: '))
            data1 = ld.add_average(ld.load_data(file1, (attr1, valu1)))
        if data1 != []:
            print('Data loaded')
        else:
            print('Invalid command')
    elif input1 == 'S' or input1 == 's':
        attr2 = input(
            "Please eneter the attribute you want to use for sorting:\n'Age'    'StudyTime'    'Failures'    'G_Avg'\n: ")
        aord2 = input('Ascending (A) of Decending (D) order: ')
        sort2 = sort.sort(data1, aord2, attr2)
        if data1 == []:
            print('File not loaded. Please, load a file first.')
        elif attr2 == attr1:
            print('Invalid command.')
        elif (attr2 == 'Age' or attr2 == 'StudyTime' or attr2 == 'Failures' or attr2 == 'G_Avg') and (aord2 == 'A' or aord2 == 'D'):
            yorn = input('Data Sorted. Do you want to display the data?: ')
            if yorn == 'Y':
                print(sort2)
        else:
            print('Invalid command.')
    elif input1 == 'C' or input1 == 'c':
        attr3 = input('Please enter the attribute you want to use to find the best fit for G_Avg: ')
        ordr3 = int(input(
            'Please enter the order of the polynomial to be fitted: '))
        if data1 == []:
            print('File not loaded. Please, load a file first.')
        elif attr3 == attr1:
            print('Invalid command.')
        elif (attr3 == 'Age' or attr3 == 'StudyTime' or attr3 == 'Failures' or attr3 == 'G_Avg') and (1 <= ordr3 <= 5):
            print(cf.curve_fit(data1, attr3, ordr3))
        else:
            print('Invalid command.')
    elif input1 == 'H' or input1 == 'h':
        attr4 = input('Please enter the attribute you want to use for plotting: ')
        if data1 == []:
            print('File not loaded. Please, load a file first.')
        elif attr4 == attr1:
            print('Invalid command.')
        elif attr4 == 'Age' or attr4 == 'StudyTime' or attr4 == 'Failures' or attr4 == 'G_Avg':
            hst.histogram(data1, attr4)
        else:
            print('Invalid command.')
    elif input1 == 'E' or input1 == 'e':
        print("Program exitted")
        condition = False