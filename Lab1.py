def add_two_numbers():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 + num2
    print(f"The sum of {num1} and {num2} is: {result}")

def subtract_two_numbers():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 - num2
    print(f"The difference between {num1} and {num2} is: {result}")

def multiply_two_numbers():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 * num2
    print(f"The product of {num1} and {num2} is: {result}")

def divide_two_numbers():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    if num2 != 0:
        result = num1 / num2
        print(f"The result of dividing {num1} by {num2} is: {result}")
    else:
        print("Error: Cannot divide by zero.")

def add_multiply_subtract_divide():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    if num2 != 0:
        division = num1 / num2
    else:
        division = "Cannot divide by zero."
    print(f"Addition: {addition}")
    print(f"Subtraction: {subtraction}")
    print(f"Multiplication: {multiplication}")
    print(f"Division: {division}")

def hours_to_minutes():
    hours = float(input("Enter time in hours: "))
    minutes = hours * 60
    print(f"{hours} hours is equal to {minutes} minutes.")

def minutes_to_hours():
    minutes = float(input("Enter time in minutes: "))
    hours = minutes / 60
    print(f"{minutes} minutes is equal to {hours} hours.")

def dollars_to_rs():
    dollars = float(input("Enter amount in dollars: "))
    rs = dollars * 48
    print(f"{dollars} dollars is equal to {rs} Rs.")

def rs_to_dollars():
    rs = float(input("Enter amount in Rs: "))
    dollars = rs / 48
    print(f"{rs} Rs. is equal to {dollars} dollars.")

def dollars_to_pounds():
    dollars = float(input("Enter amount in dollars: "))
    pounds = (dollars * 48) / 70
    print(f"{dollars} dollars is equal to {pounds} pounds.")

def grams_to_kg():
    grams = float(input("Enter weight in grams: "))
    kg = grams / 1000
    print(f"{grams} grams is equal to {kg} kg.")

def kgs_to_grams():
    kgs = float(input("Enter weight in kilograms: "))
    grams = kgs * 1000
    print(f"{kgs} kg is equal to {grams} grams.")

def bytes_to_kb_mb_gb():
    bytes = int(input("Enter size in bytes: "))
    kb = bytes / 1024
    mb = kb / 1024
    gb = mb / 1024
    print(f"{bytes} bytes is equal to {kb} KB, {mb} MB, {gb} GB.")

def celsius_to_fahrenheit():
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (9/5) * celsius + 32
    print(f"{celsius}°C is equal to {fahrenheit}°F.")

def fahrenheit_to_celsius():
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (5/9) * (fahrenheit - 32)
    print(f"{fahrenheit}°F is equal to {celsius}°C.")

def calculate_interest():
    principal = float(input("Enter principal amount: "))
    rate = float(input("Enter rate of interest: "))
    time = float(input("Enter time in years: "))
    interest = (principal * rate * time) / 100
    print(f"The calculated interest is: {interest}")

def square_area_perimeter():
    side = float(input("Enter side length of the square: "))
    area = side ** 2
    perimeter = 4 * side
    print(f"The area of the square is {area} and the perimeter is {perimeter}.")

def rectangle_area_perimeter():
    length = float(input("Enter length of the rectangle: "))
    breadth = float(input("Enter breadth of the rectangle: "))
    area = length * breadth
    perimeter = 2 * (length + breadth)
    print(f"The area of the rectangle is {area} and the perimeter is {perimeter}.")

def circle_area():
    radius = float(input("Enter radius of the circle: "))
    area = (22/7) * radius * radius
    print(f"The area of the circle is {area}.")

def triangle_area():
    height = float(input("Enter height of the triangle: "))
    length = float(input("Enter length of the base of the triangle: "))
    area = (height * length) / 2
    print(f"The area of the triangle is {area}.")

def net_salary():
    gross_salary = float(input("Enter gross salary: "))
    allowance = 0.1 * gross_salary
    deduction = 0.03 * gross_salary
    net_salary = gross_salary + allowance - deduction
    print(f"The net salary is {net_salary}.")

def net_sales():
    gross_sales = float(input("Enter gross sales amount: "))
    net_sales = gross_sales - (0.1 * gross_sales)
    print(f"The net sales after 10% discount is {net_sales}.")

def average_and_total():
    subject1 = float(input("Enter marks of subject 1: "))
    subject2 = float(input("Enter marks of subject 2: "))
    subject3 = float(input("Enter marks of subject 3: "))
    total = subject1 + subject2 + subject3
    average = total / 3
    print(f"Total marks: {total}, Average marks: {average}")

def swap_values():
    a = float(input("Enter first value: "))
    b = float(input("Enter second value: "))
    a, b = b, a
    print(f"After swapping: First value = {a}, Second value = {b}")

# Main program loop with menu
def main():
    while True:
        print("\nSelect an operation:")
        print("1. Add two numbers")
        print("2. Subtract two numbers")
        print("3. Multiply two numbers")
        print("4. Divide two numbers")
        print("5. Add, multiply, subtract, and divide two numbers")
        print("6. Convert hours into minutes")
        print("7. Convert minutes into hours")
        print("8. Convert dollars into Rs. (1$ = 48 Rs.)")
        print("9. Convert Rs. into dollars (1$ = 48 Rs.)")
        print("10. Convert dollars into pounds (1$ = 48 Rs., 1 pound = 70 Rs.)")
        print("11. Convert grams into kg")
        print("12. Convert kgs into grams")
        print("13. Convert bytes into KB, MB, and GB")
        print("14. Convert Celsius into Fahrenheit")
        print("15. Convert Fahrenheit into Celsius")
        print("16. Calculate interest")
        print("17. Calculate area & perimeter of a square")
        print("18. Calculate area & perimeter of a rectangle")
        print("19. Calculate area of a circle")
        print("20. Calculate area of a triangle")
        print("21. Calculate net salary")
        print("22. Calculate net sales")
        print("23. Calculate average of three subjects along with their total")
        print("24. Swap two values")
        print("25. Exit")
        
        choice = int(input("Enter your choice (1-25): "))
        
        if choice == 1:
            add_two_numbers()
        elif choice == 2:
            subtract_two_numbers()
        elif choice == 3:
            multiply_two_numbers()
        elif choice == 4:
            divide_two_numbers()
        elif choice == 5:
            add_multiply_subtract_divide()
        elif choice == 6:
            hours_to_minutes()
        elif choice == 7:
            minutes_to_hours()
        elif choice == 8:
            dollars_to_rs()
        elif choice == 9:
            rs_to_dollars()
        elif choice == 10:
            dollars_to_pounds()
        elif choice == 11:
            grams_to_kg()
        elif choice == 12:
            kgs_to_grams()
        elif choice == 13:
            bytes_to_kb_mb_gb()
        elif choice == 14:
            celsius_to_fahrenheit()
        elif choice == 15:
            fahrenheit_to_celsius()
        elif choice == 16:
            calculate_interest()
        elif choice == 17:
            square_area_perimeter()
        elif choice == 18:
            rectangle_area_perimeter()
        elif choice == 19:
            circle_area()
        elif choice == 20:
            triangle_area()
        elif choice == 21:
            net_salary()
        elif choice == 22:
            net_sales()
        elif choice == 23:
            average_and_total()
        elif choice == 24:
            swap_values()
        elif choice == 25:
            print("Exiting program.")
            break
        else:
            print("Invalid choice, please try again.")

# Run the main program loop
if __name__ == "__main__":
    main()
