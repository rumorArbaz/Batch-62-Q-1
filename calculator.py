# for addition
def add(a, b):
    return a + b

# for subtraction
def subtract(a, b):
    return a - b

# for multiplication
def multiply(a, b):
    return a * b

# division
def divide(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    else:
        return a / b

# Function to display the menu
def show_menu():
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

def get_user_input():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        return num1, num2
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return None, None

def calculator():
    while True:
        show_menu()

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '5':
            print("Exiting the calculator. Goodbye!")
            break
        
        num1, num2 = get_user_input()
        if num1 is None or num2 is None:
            continue
        
        if choice == '1':
            result = add(num1, num2)
            print(f"The result of {num1} + {num2} is {result}")
        elif choice == '2':
            result = subtract(num1, num2)
            print(f"The result of {num1} - {num2} is {result}")
        elif choice == '3':
            result = multiply(num1, num2)
            print(f"The result of {num1} * {num2} is {result}")
        elif choice == '4':
            result = divide(num1, num2)
            print(f"The result of {num1} / {num2} is {result}")
        else:
            print("Invalid choice! Please select a valid operation (1/2/3/4/5).")

# Run the calculator
if __name__ == "__main__":
    calculator()
