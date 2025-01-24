def largest_smallest_two():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    if num1 > num2:
        print(f"Largest: {num1}, Smallest: {num2}")
    else:
        print(f"Largest: {num2}, Smallest: {num1}")

def largest_smallest_three():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))
    
    largest = num1
    smallest = num1
    
    if num2 > largest:
        largest = num2
    if num3 > largest:
        largest = num3
    
    if num2 < smallest:
        smallest = num2
    if num3 < smallest:
        smallest = num3
    
    print(f"Largest: {largest}, Smallest: {smallest}")

def odd_or_even():
    num = int(input("Enter a number: "))
    
    if num % 2 == 0:
        print(f"{num} is Even.")
    else:
        print(f"{num} is Odd.")

def divisible_by_ten():
    num = int(input("Enter a number: "))
    
    if num % 10 == 0:
        print(f"{num} is divisible by 10.")
    else:
        print(f"{num} is not divisible by 10.")

def check_age():
    age = int(input("Enter your age: "))
    
    if age < 18:
        print("Minor")
    else:
        print("Major")

def number_of_digits():
    num = input("Enter a number: ")
    print(f"The number of digits in {num} is: {len(num)}")

def leap_year():
    year = int(input("Enter a year: "))
    
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")

def valid_triangle():
    angle1 = int(input("Enter the first angle: "))
    angle2 = int(input("Enter the second angle: "))
    angle3 = int(input("Enter the third angle: "))
    
    if angle1 + angle2 + angle3 == 180:
        print("The triangle is valid.")
    else:
        print("The triangle is not valid.")

def absolute_value():
    num = float(input("Enter a number: "))
    print(f"The absolute value of {num} is {abs(num)}.")

def rectangle_area_vs_perimeter():
    length = float(input("Enter the length of the rectangle: "))
    breadth = float(input("Enter the breadth of the rectangle: "))
    
    area = length * breadth
    perimeter = 2 * (length + breadth)
    
    if area > perimeter:
        print("Area is greater than Perimeter.")
    else:
        print("Area is not greater than Perimeter.")

def points_on_straight_line():
    x1, y1 = map(int, input("Enter x1, y1: ").split())
    x2, y2 = map(int, input("Enter x2, y2: ").split())
    x3, y3 = map(int, input("Enter x3, y3: ").split())
    
    if (y2 - y1) * (x3 - x2) == (y3 - y2) * (x2 - x1):
        print("The points lie on a straight line.")
    else:
        print("The points do not lie on a straight line.")

import math

def point_in_circle():
    x_center, y_center, radius = map(int, input("Enter center coordinates (x, y) and radius: ").split())
    x_point, y_point = map(int, input("Enter the point's coordinates (x, y): ").split())
    
    distance = math.sqrt((x_point - x_center) ** 2 + (y_point - y_center) ** 2)
    
    if distance < radius:
        print("The point lies inside the circle.")
    elif distance == radius:
        print("The point lies on the circle.")
    else:
        print("The point lies outside the circle.")

def number_to_word():
    num = int(input("Enter a number between 0 and 19: "))
    words = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
    ]
    if 0 <= num <= 19:
        print(f"The number {num} in words is: {words[num]}")
    else:
        print("Please enter a number between 0 and 19.")

def grade_and_pass_fail():
    subject1 = int(input("Enter marks of subject 1: "))
    subject2 = int(input("Enter marks of subject 2: "))
    subject3 = int(input("Enter marks of subject 3: "))
    
    total = subject1 + subject2 + subject3
    average = total / 3
    
    def get_grade(marks):
        if marks == 0:
            return "NA"
        elif marks <= 39:
            return "F"
        elif marks <= 44:
            return "P"
        elif marks <= 49:
            return "C"
        elif marks <= 54:
            return "B"
        elif marks <= 59:
            return "B+"
        elif marks <= 69:
            return "A"
        elif marks <= 79:
            return "A+"
        elif marks <= 100:
            return "O"
    
    grade1 = get_grade(subject1)
    grade2 = get_grade(subject2)
    grade3 = get_grade(subject3)
    
    if subject1 <= 39 or subject2 <= 39 or subject3 <= 39:
        result = "Fail"
    else:
        result = "Pass"
    
    print(f"Total Marks: {total}, Average: {average}")
    print(f"Grades: Subject 1: {grade1}, Subject 2: {grade2}, Subject 3: {grade3}")
    print(f"Result: {result}")

# Main menu function to select the program to run.
def main_menu():
    while True:
        print("\nSelect an option to run the program:")
        print("1. Largest and Smallest values out of two")
        print("2. Largest and Smallest values out of three")
        print("3. Check Odd or Even")
        print("4. Check divisibility by 10")
        print("5. Check Major or Minor")
        print("6. Number of Digits")
        print("7. Leap Year Check")
        print("8. Valid Triangle Check")
        print("9. Absolute Value")
        print("10. Rectangle Area vs Perimeter")
        print("11. Points on a Straight Line")
        print("12. Point Inside Circle")
        print("13. Number to Word Conversion")
        print("14. Grade and Pass/Fail Check")
        print("15. Exit")

        choice = int(input("Enter your choice (1-15): "))

        if choice == 1:
            largest_smallest_two()
        elif choice == 2:
            largest_smallest_three()
        elif choice == 3:
            odd_or_even()
        elif choice == 4:
            divisible_by_ten()
        elif choice == 5:
            check_age()
        elif choice == 6:
            number_of_digits()
        elif choice == 7:
            leap_year()
        elif choice == 8:
            valid_triangle()
        elif choice == 9:
            absolute_value()
        elif choice == 10:
            rectangle_area_vs_perimeter()
        elif choice == 11:
            points_on_straight_line()
        elif choice == 12:
            point_in_circle()
        elif choice == 13:
            number_to_word()
        elif choice == 14:
            grade_and_pass_fail()
        elif choice == 15:
            print("Exiting program.")
            break
        else:
            print("Invalid choice, please try again.")

# Call the main menu to run the program
main_menu()
