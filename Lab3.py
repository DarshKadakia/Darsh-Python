# 1. Count how many vowels are there in a string.
def count_vowels():
    string = input("Enter a string: ")
    vowels = "aeiouAEIOU"
    count = 0
    
    for char in string:
        if char in vowels:
            count += 1
    
    print(f"Total vowels in the string: {count}")

# 2. Write functions to convert a string to lower case, upper case, and toggle case.
def to_lower_case():
    string = input("Enter a string: ")
    result = ""
    for char in string:
        if 'A' <= char <= 'Z':
            result += chr(ord(char) + 32)
        else:
            result += char
    print(f"Lowercase: {result}")

def to_upper_case():
    string = input("Enter a string: ")
    result = ""
    for char in string:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char
    print(f"Uppercase: {result}")

def toggle_case():
    string = input("Enter a string: ")
    result = ""
    for char in string:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        elif 'A' <= char <= 'Z':
            result += chr(ord(char) + 32)
        else:
            result += char
    print(f"Toggled case: {result}")

# 3. Check whether one string is there in another string.
def check_substring():
    string1 = input("Enter the first string: ")
    string2 = input("Enter the second string: ")
    
    if string2 in string1:
        print(f"'{string2}' is found in '{string1}'.")
    else:
        print(f"'{string2}' is not found in '{string1}'.")

# 4. Removes one string from another string.
def remove_substring():
    string1 = input("Enter the main string: ")
    string2 = input("Enter the string to remove: ")
    
    result = string1.replace(string2, "")
    print(f"String after removal: {result}")

# Main menu function to select the program to run.
def main_menu():
    while True:
        print("\nSelect an option to run the program:")
        print("1. Count vowels in a string")
        print("2. Convert string to lowercase")
        print("3. Convert string to uppercase")
        print("4. Toggle case of string")
        print("5. Check if one string is present in another")
        print("6. Remove one string from another string")
        print("7. Exit")

        choice = int(input("Enter your choice (1-7): "))

        if choice == 1:
            count_vowels()
        elif choice == 2:
            to_lower_case()
        elif choice == 3:
            to_upper_case()
        elif choice == 4:
            toggle_case()
        elif choice == 5:
            check_substring()
        elif choice == 6:
            remove_substring()
        elif choice == 7:
            print("Exiting program.")
            break
        else:
            print("Invalid choice, please try again.")

# Call the main menu to run the program
main_menu()
