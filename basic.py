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
    
#print(check_leap_year(year))

#Sum of Even Numbers: Write a program that calculates the sum of all even numbers from 1 to a given number n (inclusive).

def even_num_sum(stop):
    total = 0
    for num in range(stop):
        if num % 2 == 0:
            total += num
    return total

#print(even_num_sum(10))

#Multiplication Table: Create a program that prints a multiplication table for a given number up to 10. 

def multi_table(value):
    for num in range(1, 11):
        total = value * num
        print(f'{value} x {num} = {total}')
    
#print(multi_table(7))

# Shopping list manager

class ShoppingList:
    def __init__(self, item):
        self.shop_list = [item]

    def add_item(self, item):
        self.shop_list.append(item)
        print(f'Added: {item} to list')

    def display_items(self):
        for item in self.shop_list:
            print(item)

    def remove_item(self, item):
        self.shop_list.remove(item)
        print(f'Removed {item} from list')

# shop = ShoppingList('Bread')
# shop.add_item('Butter')
# shop.add_item('Baking soda')

# shop.display_items()
# shop.remove_item('Bread')
# shop.display_items()

student_records = {}
stud_avg = {}


#Student Records Build a dictionary to store student information (name, age, grades as a list). 
def add_student(name, age, grd1, grd2, grd3):
    student_records[name] = {'Age': age,
                             'Grades': [grd1, grd2, grd3]
                             }
    
def clac_avg(name):
    num_of_grd = len(student_records[name]['Grades'])
    all_grd = sum(student_records[name]['Grades'])

    avg = all_grd / num_of_grd
    stud_avg[name] = avg
    return avg

def highest_avg():
    avgs = list(stud_avg.values())
    names = list(stud_avg.keys())
    max = avgs[0]
    name = names[0]
    for key, value in stud_avg.items():
        if value > max:
            max = value
            name = key
    return name
    

add_student('Justin', 18,75,80,50)
add_student('Kim', 22, 45, 45, 30)

print(clac_avg('Justin'))
print(clac_avg('Kim'))

print(highest_avg())