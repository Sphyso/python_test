#Grade Calculator: Takes a student's numerical score (0-100) and prints their letter grade:
grade = 89
def grade_calculator(grade):
    if grade >= 90 and grade <= 100:
        return 'A'
    elif grade >= 80 and grade < 90:
        return 'B'
    elif grade >= 70 and grade < 80:
        return 'C'
    elif grade >= 60 and grade < 70:
        return 'D'
    elif grade >= 50 and grade < 60:
        return 'E'
    elif grade < 50 and grade >= 0:
        return 'F'
    else:
        return 'Invalid input'
    
def grade_calcultor_switch(grade):
    match grade:
        case s if 90 <= grade <= 100:
            return 'A'
        case s if 80 <= grade < 90:
            return 'B' 
        case s if 70 <= grade < 80:
            return 'C'
        case s if 60 <= grade < 70:
            return 'D'
        case s if 50 <= grade < 60:
            return 'E'
        case s if 0 <= grade < 50:
            return 'F'
        case _:
            print('What!')
    
#print('You got:', grade_calcultor_switch(grade))

#Leap Year Checker: Create a program that determines if a year is a leap year.
year = 2000
def check_leap_year(year):
    if year % 400 == 0 and year % 100 == 0:
        return 'Leap year'
    elif year % 4 == 0 and year % 100 != 0:
        return 'Leap year'
    else:
        return 'Not leap'
    
print(check_leap_year(year))