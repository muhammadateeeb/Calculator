import math

def get_valid_choice():
    while True:
        choice = input("Which Operation Do You Want: Factorial, Arithmetic, Trigonometric, Logarithmic, Nth Root, Unit Conversion , Percentage , or type 'exit' to quit? ").lower()
        if choice in ['factorial', 'arithmetic', 'trigonometric', 'logarithmic', 'nth root', 'percentage' ,'unit conversion'  , 'exit']:
            return choice
        else:
            print("Invalid choice! Please enter 'Factorial', 'Arithmetic', 'Trigonometric', 'Logarithmic', 'Nth Root', 'Unit Conversion', 'percentage' or 'exit'.")

def get_valid_operator():
    valid_operators = ['+', '-', '*', '/', '%', 'sqrt', 'expo']
    while True:
        operator = input("Enter The Operation You Want To Perform (+, -, *, /, %, sqrt, expo): ").lower()
        if operator in valid_operators:
            return operator
        else:
            print("Invalid operator! Please enter a valid operator.")
            
def percentage():
    while True:
        try:
            total = float(input("Enter the total value (positive number): "))
            if total <= 0:
                print("Total value must be a positive number.")
                continue

            percent = float(input("Enter the percentage you want to calculate (between 0 and 100): "))
            if percent < 0 or percent > 100:
                print("Percentage must be between 0 and 100.")
                continue

            result = (total * percent) / 100
            print(f"{percent}% of {total} is {result}")
            break  # Exit after successful calculation

        except ValueError:
            print("Invalid input! Please enter a valid number.")



def valid_input_number():
    while True:
        try:
            number = int(input("Enter The Number To Find Factorial: "))
            return number
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

def valid_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            
def unit_conversion():
    while True:
        choice = input("Choose conversion: 'km to miles' or 'C to F': ").strip().lower()
        
        if choice == 'km to miles':
            while True:
                try:
                    km = float(input("Enter kilometers (positive number): "))
                    if km < 0:
                        print("Please enter a positive number for kilometers.")
                    else:
                        miles = km * 0.621371
                        print(f"{km} kilometers is {miles} miles")
                        break  # Exit the loop after successful conversion
                except ValueError:
                    print("Invalid input! Please enter a valid number.")

        elif choice == 'c to f':
            while True:
                try:
                    celsius = float(input("Enter Celsius (a number): "))
                    fahrenheit = (celsius * 9/5) + 32
                    print(f"{celsius}°C is {fahrenheit}°F")
                    break  # Exit the loop after successful conversion
                except ValueError:
                    print("Invalid input! Please enter a valid number.")
        
        else:
            print("Invalid conversion choice. Please choose either 'km to miles' or 'C to F'.")
            continue  # Loop back to ask for a valid choice
        break  # Exit the outer loop after a successful choice and conversion


def valid_log_input():
    while True:
        try:
            n = int(input("Enter The Number You want to find the logarithm of: "))
            if n > 0:
                return n
            else:
                print("Please Enter a Positive Number :)")
        except ValueError:
            print("Please Enter a Valid Integer :)")

def get_valid_input_root():
    while True:
        try:
            x = float(input("Enter the number: "))
            n = int(input("Enter the root (positive integer): "))
            if n > 0:
                return x, n
            else:
                print("The root must be a positive integer.")
        except ValueError:
            print("Invalid input! Please enter a valid number and positive integer.")

def factorial(n):
    result = 1
    for x in range(n, 1, -1):
        result *= x
    return result

def nth_root(x, n):
    return x ** (1/n)

def perform_arithmetic():
    operator = get_valid_operator()
    
    if operator != 'sqrt':  # If the operator is not square root, we need two numbers
        a = valid_float_input("Enter The First Number: ")
        b = valid_float_input("Enter The Second Number: ")
    else:  # For square root, we need only one number
        a = valid_float_input("Enter the number for square root: ")

    # Perform the calculation based on the operator
    if operator == '+':
        result = a + b
        print(f"Your Sum is = {result}")
    elif operator == '-':
        result = a - b
        print(f"Your Difference is = {result}")
    elif operator == '/':
        if b != 0:
            result = a / b
            print(f"Your Division is = {result}")
        else:
            print("Cannot divide by Zero :(")
    elif operator == '*':
        result = a * b
        print(f"Your Product is = {result}")
    elif operator == '%':
        if b != 0:
            result = a % b
            print(f"Your Remainder is = {result}")
        else:
            print("Cannot divide by zero :(")
    elif operator == 'sqrt':
        result = math.sqrt(a)
        print(f"The Square Root is = {result}")
    elif operator == 'expo':
        result = a ** b
        print(f"Your Exponential is = {result}")

def perform_trigonometric():
    # Define the trigonometric values in a dictionary
    trig_values = {
        'sin': {0: '0', 30: '1/2', 45: '1/√2', 60: '3/√2', 90: '1'},
        'cos': {0: '1', 30: '3/√2', 45: '1/√2', 60: '1/2', 90: '0'},
        'tan': {0: '0', 30: '1/√3', 45: '1', 60: '√3', 90: '∞'},
        'cosec': {0: '∞', 30: '2', 45: '√2', 60: '2/√3', 90: '1'},
        'sec': {0: '1', 30: '2/√3', 45: '√2', 60: '2', 90: '∞'},
        'cot': {0: '∞', 30: '√3', 45: '1', 60: '1/√3', 90: '0'}
    }

    # Input from user
    ratio = input("Enter the Ratio (sin, cos, tan, cosec, sec, cot): ").lower()
    while ratio not in trig_values:
        print("Invalid ratio! Please enter a valid ratio.")
        ratio = input("Enter the Ratio (sin, cos, tan, cosec, sec, cot): ").lower()

    while True:
        try:
            angle = int(input("Now Enter The Angle (0, 30, 45, 60, 90): "))
            if angle in trig_values[ratio]:
                break
            else:
                print("Invalid angle! Please enter a valid angle (0, 30, 45, 60, 90).")
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

    print(f"{ratio}({angle}) = {trig_values[ratio][angle]}")

# Main program logic
while True:
    choice = get_valid_choice()

    # Exit option
    if choice == 'exit':
        print("Exiting the calculator. Goodbye!")
        break

    if choice == 'factorial':
        number = valid_input_number()
        if number >= 0:
            factorial_result = factorial(number)
            print(f"The Factorial of {number} is = {factorial_result}")
        else:
            print("Factorial is only defined for non-negative integers.")

    elif choice == 'arithmetic':
        perform_arithmetic()
    
    elif choice == 'unit conversion':
        # Call the function to test it
        unit_conversion()
        print("Tannk You :)")

    elif choice == 'trigonometric':
        perform_trigonometric()
    elif choice == 'percentage':
        percentage()
        print("Thanks :) ")
        

    elif choice == 'logarithmic':
        valid_number = valid_log_input()
        
        # Get the base and handle empty input correctly
        base = input("Enter the Base (Default: natural, or 10): ").strip().lower()

        if base == 'natural' or base == "":
            result = math.log(valid_number)  # Natural log
            base = "natural (base e)"  # Correct label for the base
        elif base == '10':
            result = math.log10(valid_number)  # Base-10 log
        else:
            result = None
            print("Invalid base. Please enter 'natural' or '10'.")

        if result is not None:
            print(f"The Log of {valid_number} with the Base {base} is {result}")

    elif choice == 'nth root':
        x, n = get_valid_input_root()
        if x < 0 and n % 2 == 0:
            print("Cannot calculate even root of a negative number.")
        else:
            result = nth_root(x, n)
            print(f"The {n}th root of {x} is {result}.")

    # After each operation, prompt the user to continue
    print("\n")
history = []

def save_to_history(operation, result):
    history.append(f"{operation} = {result}")

def show_history():
    if history:
        print("Calculation History:")
        for record in history:
            print(record)
    else:
        print("No history available.")
