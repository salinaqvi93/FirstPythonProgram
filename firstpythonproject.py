from statistics import mean
import time as t

studentGrades = {'ali':[11]}

def ShowPrompt():
    print('Welcome to Grade Central')
    print('\n')
    print('[1] - Enter Grades')
    print('[2] - Remove Student')
    print('[3] - Student Average Grades')
    print('[4] - Exit')
    print('\n')
    return input('What would you like to do today? (Enter a number) ')

def AddGrade(student, grade):
    if student in studentGrades:
        studentGrades[student].append(grade)
    else:
        studentGrades[student] = []
        studentGrades[student].append(grade)
    print('Adding Grade...')
    print(studentGrades)

def RemoveStudent(student):
    del studentGrades[student]
    print('Removing Student...')
    print(studentGrades)

def CalculateAverageGrade(student):
    if student in studentGrades:
        print(student + ': ' + str(mean(studentGrades[student])))
    else:
        print('Student does not exists\n')

username = input('Username: ')
password = input('Password: ')
if ( username == 'python' and password == '999'):
    while (1):
        try:
            userInput = ShowPrompt()
            if(userInput == '1'):
                student = input('Student Name: ')
                grade = int(input('Grade: '))
                AddGrade(student,grade)
            elif(userInput == '2'):
                student = input('What student to remove?: ')
                RemoveStudent(student)
            elif(userInput == '3'):
                student = input('Whose average to calculate?: ')
                CalculateAverageGrade(student)
            elif(userInput == '4'):
                print('Exiting...')
                break
            else:
                print('Enter a valid number\n')
        except Exception as e:
            print(e)
else:
    print('Invalid Login, Detonating in 5 seconds!')
    t.sleep(5)
    print('Aborting...')

