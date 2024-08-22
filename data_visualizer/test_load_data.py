# ECOR 1042 Lab 4 - team submission

#import check module here
import check
#import load_data module here
import load_data

# Update "" with your the name of the active members of the team
__author__ = "Teghbir Chadha, Michael Acquah, Tyler Knox, Yahia Omeman"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T99"

#==========================================#

# Place test_return_list function here 
def test_return_list():
    
    # test that student_school_list returns a list (3 different test cases required)
    check.equal(isinstance(load_data.student_school_list(
        'student-test.csv', 'GP'), list), True)
    check.equal(isinstance(load_data.student_school_list(
        'student-test.csv', 'MS'), list), True)
    check.equal(isinstance(load_data.student_school_list(
        'student-test.csv', 'MB'), list), True)

    # test that student_age_list returns a list (3 different test cases required)
    check.equal(isinstance(load_data.student_age_list(
        'student-test.csv', '18'), list), True)
    check.equal(isinstance(load_data.student_age_list(
        'student-test.csv', '17'), list), True)
    check.equal(isinstance(load_data.student_age_list(
        'student-test.csv', '16'), list), True)

    # test that student_health_list returns a list (3 different test cases required)
    check.equal(isinstance(load_data.student_health_list(
        'student-test.csv', '3'), list), True)
    check.equal(isinstance(load_data.student_health_list(
        'student-test.csv', '4'), list), True)
    check.equal(isinstance(load_data.student_health_list(
        'student-test.csv', '5'), list), True)

    # test that student_failure_list returns a list (3 different test cases required)
    check.equal(isinstance(load_data.student_failures_list(
        'student-test.csv', '0'), list), True)
    check.equal(isinstance(load_data.student_failures_list(
        'student-test.csv', '2'), list), True)
    check.equal(isinstance(load_data.student_failures_list(
        'student-test.csv', '3'), list), True)

    # test that load_data returns a list (6 different test cases required)
    check.equal(isinstance(load_data.load_data(
        'student-test.csv', ('School', "GP")), list), True)
    check.equal(isinstance(load_data.load_data(
        'student-test.csv', ('Age', 18)), list), True)
    check.equal(isinstance(load_data.load_data(
        'student-test.csv', ('School', "MB")), list), True)
    check.equal(isinstance(load_data.load_data(
        'student-test.csv', ('Failures', 3)), list), True)
    check.equal(isinstance(load_data.load_data(
        'student-test.csv', ('Health', 6)), list), True)
    check.equal(isinstance(load_data.load_data(
        'student-test.csv', ("Failures", 0)), list), True)

    # test that add_average returns a list (3 different test cases required)
    check.equal(isinstance(load_data.add_average(
        load_data.student_age_list('student-test.csv', 15)), list), True)
    check.equal(isinstance(load_data.add_average(
        load_data.student_health_list('student-test.csv', 3)), list), True)
    check.equal(isinstance(load_data.add_average(
        load_data.student_failures_list('student-test.csv', 0)), list), True)

    check.summary()

# Place test_return_list_correct_lenght function here
def test_return_list_correct_length():
    
    #test that student_school_list returns a list with the correct lenght (3 different test cases required)
    check.equal(len(load_data.student_school_list('student-test.csv',"GP")),3)
    check.equal(len(load_data.student_school_list('student-test.csv',"MB")),2)
    check.equal(len(load_data.student_school_list('student-test.csv',"MS")),4)
    
    #test that student_age_list returns a list  with the correct lenght (3 different test cases required)
    check.equal(len(load_data.student_age_list('student-test.csv',18)),4)
    check.equal(len(load_data.student_age_list('student-test.csv',17)),6)
    check.equal(len(load_data.student_age_list('student-test.csv',15)),3)    
    
    #test that student_health_list returns a list  with the correct lenght (3 different test cases required)
    check.equal(len(load_data.student_health_list('student-test.csv',3)),8)
    check.equal(len(load_data.student_health_list('student-test.csv',5)),3)
    check.equal(len(load_data.student_health_list('student-test.csv',4)),3)    
    
    #test that student_failures_list returns a list   with the correct lenght(3 different test cases required)
    check.equal(len(load_data.student_failures_list('student-test.csv',0)),11)
    check.equal(len(load_data.student_failures_list('student-test.csv',3)),1)
    check.equal(len(load_data.student_failures_list('student-test.csv',2)),2)
    
    #test that load_data returns a list  with the correct lenght (6 different test cases required)
    check.equal(len(load_data.load_data('student-test.csv',('School','Pizza'))),0)
    check.equal(len(load_data.load_data('student-test.csv',('School','GP'))),3)
    check.equal(len(load_data.load_data('student-test.csv',('Age',18))),4)
    check.equal(len(load_data.load_data('student-test.csv',('Age',17))),6)
    check.equal(len(load_data.load_data('student-test.csv',('All',1292929))),15)
    check.equal(len(load_data.load_data('student-test.csv',('Health', 1999))),0)
    
    #test that add_average returns a list   with the correct lenght (3 different test cases required)
    check.equal(len(load_data.add_average(load_data.load_data('student-test.csv',("All",0)))),15)
    check.equal(len(load_data.add_average(load_data.load_data('student-test.csv',('School','GP')))),3)
    check.equal(len(load_data.add_average(load_data.load_data('student-test.csv',('Health', 1999)))),0)
    
    check.summary()

#Place test_return_correct_dict_inside_list function here
def test_return_correct_dict_inside_list():
    #school list (3cases)
    check.equal(load_data.student_school_list('student-test.csv',"GP")[0] and load_data.student_school_list('student-test.csv',"GP")[-1], {'Age':18, 'StudyTime':2, 'Failures': 0, 'Health':3, 'Absences':6, 'G1':5, 'G2':6, 'G3':6} and {'Age':15, 'StudyTime':2, 'Failures': 3, 'Health':3, 'Absences':10, 'G1':7, 'G2':8, 'G3':10})
    check.equal(load_data.student_school_list('student-test.csv',"MB")[0] and load_data.student_school_list('student-test.csv',"MB")[-1], {'Age':16, 'StudyTime':2, 'Failures': 0, 'Health':3, 'Absences':12, 'G1':5, 'G2':5, 'G3':5} and {'Age':15, 'StudyTime':1, 'Failures': 0, 'Health':3, 'Absences':2, 'G1':10, 'G2':12, 'G3':12})
    check.equal(load_data.student_school_list('student-test.csv',"JP"),[])
    
    #age list (3cases)
    check.equal(load_data.student_age_list('student-test.csv',18)[0] and load_data.student_age_list('student-test.csv',18)[-1], {'School':"GP", 'StudyTime':2, 'Failures': 0, 'Health':3, 'Absences':6, 'G1':5, 'G2':6, 'G3':6} and {'School':'MS', 'StudyTime':3, 'Failures': 0, 'Health':5, 'Absences':2, 'G1':9, 'G2':8, 'G3':8})
    check.equal(load_data.student_age_list('student-test.csv',17)[0] and load_data.student_age_list('student-test.csv',17)[-1], {'School':"GP", 'StudyTime':2, 'Failures': 0, 'Health':3, 'Absences':4, 'G1':5, 'G2':5, 'G3':6} and {'School':'MS', 'StudyTime':3, 'Failures': 0, 'Health':4, 'Absences':4, 'G1':14, 'G2':14, 'G3':14})    
    check.equal(load_data.student_age_list('student-test.csv',35),[])   
    
    #health list (3cases)
    check.equal(load_data.student_health_list('student-test.csv',4)[0] and load_data.student_health_list('student-test.csv',4)[-1], {'School':"BD",'Age':17, 'StudyTime':3, 'Failures': 0, 'Absences':4, 'G1':10, 'G2':9, 'G3':9} and {'School':'MS', 'Age':17, 'StudyTime':3,'Failures': 0, 'Absences':4, 'G1':14, 'G2':14, 'G3':14})
    check.equal(load_data.student_health_list('student-test.csv',5)[0] and load_data.student_health_list('student-test.csv',5)[-1], {'School':"CF",'Age':16, 'StudyTime':2, 'Failures': 1, 'Absences':4, 'G1':10, 'G2':12, 'G3':12} and {'School':'MS', 'Age':18, 'StudyTime':3,'Failures': 0, 'Absences':2, 'G1':9, 'G2':8, 'G3':8})
    check.equal(load_data.student_health_list('student-test.csv',305),[])
    
    #failures list (3cases)
    check.equal(load_data.student_failures_list('student-test.csv',0)[0] and load_data.student_failures_list('student-test.csv',0)[-1], {'School':"GP",'Age':18, 'StudyTime':2, 'Health':3, 'Absences':6, 'G1':5, 'G2':6, 'G3':6} and {'School':'MS', 'Age':18, 'StudyTime':3, 'Health':5, 'Absences':2, 'G1':9, 'G2':8, 'G3':8})
    check.equal(load_data.student_failures_list('student-test.csv',2)[0] and load_data.student_failures_list('student-test.csv',2)[-1], {'School':"CF",'Age':15, 'StudyTime':5, 'Health':3, 'Absences':6, 'G1':5, 'G2':9, 'G3':7} and {'School':'CF', 'Age':17, 'StudyTime':1, 'Health':5, 'Absences':0, 'G1':7, 'G2':6, 'G3':0})
    check.equal(load_data.student_failures_list('student-test.csv',305),[])
    
    #load_data list (6 cases)
    check.equal(load_data.load_data('student-test.csv', ('School', 'GP'))[0], {'Age': 18, 'StudyTime': 2, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}) and (load_data.load_data('student-test.csv', ('School', 'GP'))[-1], {'Age': 15, 'StudyTime': 2, 'Failures': 3, 'Health': 3, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10})
    check.equal(load_data.load_data('student-test.csv', ('all', 'abcdsedd')), [])
    check.equal(load_data.load_data('student-test.csv', ('All', 0))[0], {'School': 'GP', 'Age': 18, 'StudyTime': 2, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}) and (load_data.load_data('student-test.csv', ('All', 0))[-1], {'School': 'MS', 'Age': 18, 'StudyTime': 3, 'Failures': 0, 'Health': 5, 'Absences': 2, 'G1': 9, 'G2': 8, 'G3': 8})
    check.equal(load_data.load_data('student-test.csv', ('Failures', 0))[0], {'School': 'GP', 'Age': 18, 'StudyTime': 2, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}) and (load_data.load_data('student-test.csv', ('Failures', 0))[-1], {'School': 'MS', 'Age': 18, 'StudyTime': 3, 'Health': 5, 'Absences': 2, 'G1': 9, 'G2': 8, 'G3': 8})
    check.equal(load_data.load_data('student-test.csv', ('Health', 5))[0], {'School': 'CF', 'Age': 16, 'StudyTime': 2, 'Failures': 1, 'Absences': 4, 'G1': 10, 'G2': 12, 'G3': 12}) and (load_data.load_data('student-test.csv', ('Health', 5))[-1], {'School': 'MS', 'Age': 18, 'StudyTime': 3, 'Failures': 0, 'Absences': 2, 'G1': 9, 'G2': 8,'G3': 8})
    check.equal(load_data.load_data('student-test.csv', ('Age', 18))[0], {'School': 'GP', 'StudyTime': 2, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}) and (load_data.load_data('student-test.csv', ('Age', 18))[-1], {'School': 'MS', 'StudyTime': 3, 'Failures': 0, 'Health': 5, 'Absences': 2, 'G1': 9, 'G2': 8, 'G3': 8})
    
    #add_average list (3cases)
    check.equal(load_data.add_average([{'School': 'GP', 'Age': 18, 'StudyTime': 2, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}, {'School': 'GP', 'Age': 17, 'StudyTime': 2, 'Failures': 0, 'Health': 3, 'Absences': 4, 'G1': 5, 'G2': 5, 'G3': 6}])[0], {'School': 'GP', 'Age': 18, 'StudyTime': 2, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6, 'G_Avg': 5.67}) and (load_data.add_average([{'School': 'GP', 'Age': 18, 'StudyTime': 2, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}, {'School': 'GP', 'Age': 17, 'StudyTime': 2, 'Failures': 0, 'Health': 3, 'Absences': 4, 'G1': 5, 'G2': 5, 'G3': 6}])[-1], {'School': 'GP', 'Age': 17, 'StudyTime': 2, 'Failures': 0, 'Health': 3, 'Absences': 4, 'G1': 5, 'G2': 5, 'G3': 6, 'G_Avg': 5.33})
    check.equal(load_data.add_average([{'School': 'GP', 'Age': 15, 'StudyTime': 2, 'Failures': 3, 'Health': 3, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10}, {'School': 'MB', 'Age': 16, 'StudyTime': 2, 'Failures': 0, 'Health': 3, 'Absences': 12, 'G1': 5, 'G2': 5, 'G3': 5}, {'School': 'MB', 'Age': 15, 'StudyTime': 1, 'Failures': 0, 'Health': 3, 'Absences': 2, 'G1': 10, 'G2': 12, 'G3': 12}])[0], {'School': 'GP', 'Age': 15, 'StudyTime': 2, 'Failures': 3, 'Health': 3, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10, 'G_Avg': 8.33}) and (load_data.add_average([{'School': 'GP', 'Age': 15, 'StudyTime': 2, 'Failures': 3, 'Health': 3, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10}, {'School': 'MB', 'Age': 16, 'StudyTime': 2, 'Failures': 0, 'Health': 3, 'Absences': 12, 'G1': 5, 'G2': 5, 'G3': 5}, {'School': 'MB', 'Age': 15, 'StudyTime': 1, 'Failures': 0, 'Health': 3, 'Absences': 2, 'G1': 10, 'G2': 12, 'G3': 12}])[-1], {'School': 'MB', 'Age': 15, 'StudyTime': 1, 'Failures': 0, 'Health': 3, 'Absences': 2, 'G1': 10, 'G2': 12, 'G3': 12, 'G_Avg': 11.33})
    check.equal(load_data.add_average([]), [])
    
    check.summary()
    
#Place test_add_average function here
def test_add_average():
    
    data_test = [load_data.add_average(load_data.student_school_list('student-test.csv', 'MB')),
                      load_data.add_average(load_data.student_health_list('student-test.csv',5)),
                      load_data.add_average(load_data.student_age_list('student-test.csv', 18)), 
                      load_data.add_average(load_data.student_failures_list('student-test.csv', 2)), 
                      load_data.add_average(load_data.load_data('student-test.csv', ('All', None)))]
     
    #test that the function does not change the lengh of the list provided as input parameter (5 different test cases required)
    check.equal(len(load_data.add_average([{'Age': 18, 'StudyTime': 2, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}])[0]), 9)
    check.equal(len(load_data.add_average([{'School': 'GP', 'StudyTime': 2, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}])[0]), 9)
    check.equal(len(load_data.add_average([{'School': 'GP', 'Age': 18, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}])[0]), 9)
    check.equal(len(load_data.add_average([{'School': 'GP', 'Age': 18, 'StudyTime': 2, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}])[0]), 9)
    check.equal(len(load_data.add_average([{'School': 'GP', 'Age': 18, 'StudyTime': 2, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}])[0]), 10)

    #test that the function returns an empty list when it is called whith an empty list
    check.equal(load_data.add_average([]), [],'')

    #test that the function inscrememnts the key count of the dictionary inside the list by one  (5 different test cases required)
    key_count = True
    for method in(data_test):
        for Dict in method:
            if method != data_test[4]:
                if (len(Dict)-1) != 8:
                    key_count = False
            elif method == data_test[4]:
                if (len(Dict)-1) != 9:
                    key_count = False
        check.equal((key_count), True,'')
        key_count = True
    
    #test that the G_Avg value is properly calculated  (5 different test cases required)
    average_of_G = True
    for Method in(data_test):
        for Dict in Method:
            if round(((Dict.get('G1')) + (Dict.get('G2')) + (Dict.get('G3'))) /3, 3) == Dict.get('G_Avg'):
                average_of_G = True
        check.equal((average_of_G), True)
        average_of_G = True 
    check.summary()
    


# Do NOT include a main script in your submission
