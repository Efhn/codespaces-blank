#!/usr/bin/env python
"""
Compute the average exam grade for multiple students
"""

# Obtain the number of exam grades per student
num_exams = int(input('How many exams grades does each student have?'))
# Set your initial sentinel value
more_grades = 'Y'

# TODO: Compute average exam grades until the user wants to stop
while more_grades == 'Y':
    print('Enter the exam grades: ')
    total = 0
    for exam in range(1, num_exams + 1):
        score = int(input(f'Exam {exam}: '))  # Prompt for each exam grade
        total = total + score 
    # Calculate the average
    average = total/num_exams
    print(f'The average is {average:.2f}')
    more_grades = input('Enter exam grades for anoother student: (Y/N)? ').upper() # make it upper case

print('Thank you for your input')
