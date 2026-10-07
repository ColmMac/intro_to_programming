
def add(a, b):
    result = a + b
    return result

def subtract(a, b):
    result = a - b
    return result

def divide(a, b):
    if b == 0:
        print("Error! Cannot divide by zero")
    else:
        result = a / b
        return result

def multiply(a, b):
    result = a * b
    return result 

while True:
    print("\n CALCULATOR")
    try:
        a = float(input("Please enter first number: "))
        print("1. Add")
        print("2. Subtract")
        print("3. Divide")
        print("4. Multiply")
        operation = int(input("Enter an operation from 1-4:"))
        b = float(input("Please enter second number: "))
    except ValueError:
        print("Please try again")


    if operation == 1:
        result = add(a,b)
        stringop = "+"
    elif operation == 2:
        result = subtract(a,b)
        stringop = "-"
    elif operation == 3:
        result = divide(a,b)
        stringop = "/"
    elif operation == 4:
        result = multiply(a,b)
        stringop = "*"
    print(f"{a} {stringop} {b} = {result}")

    print("\n1. To continue")
    print("2. To exit")
    try:
        quit = int(input("Please enter 1 or 2 in order to exit: "))
    except ValueError:
        print("Invalid! Please enter 1 or 2.")
    if quit == 2:
        break
    