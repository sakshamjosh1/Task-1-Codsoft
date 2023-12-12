import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Cannot divide by zero."

def power(x, y):
    return x ** y

def square_root(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return "Error: Cannot calculate square root of a negative number."

def logarithm(x, base):
    if x > 0 and base > 0 and base != 1:
        return math.log(x, base)
    else:
        return "Error: Invalid input for logarithm."

def calculator():
    print("Scientific Calculator : ")
    print("Operations : ")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponentiation")
    print("6. Square Root")
    print("7. Logarithm")
    print("8. Exit")

    while True:
        choice = input("Enter choice (1-8) : ")

        if choice in ('1', '2', '3', '4', '5', '6', '7', '8'):
            if choice == '8':
                print("Exiting the calculator. Goodbye!")
                break

            if choice in ('1', '2', '3', '4', '5', '7'):
                x = float(input("Enter first number: "))
                y = float(input("Enter second number: "))

            if choice == '6':
                x = float(input("Enter a number: "))

            if choice == '1':
                print(f"Result: {add(x, y)}")

            elif choice == '2':
                print(f"Result: {subtract(x, y)}")

            elif choice == '3':
                print(f"Result: {multiply(x, y)}")

            elif choice == '4':
                print(f"Result: {divide(x, y)}")

            elif choice == '5':
                print(f"Result: {power(x, y)}")

            elif choice == '6':
                print(f"Result: {square_root(x)}")

            elif choice == '7':
                base = float(input("Enter the base for logarithm: "))
                print(f"Result: {logarithm(x, base)}")

        else:
            print("Invalid input. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    calculator()
