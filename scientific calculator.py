import math


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y


def power(x, y):
    return x ** y


def square_root(x):
    if x < 0:
        return "Error! Negative number."
    else:
        return math.sqrt(x)


def logarithm(x, base):
    if x <= 0:
        return "Error! Non-positive number."
    else:
        return math.log(x, base)


def factorial(x):
    if x < 0:
        return "Error! Negative number."
    else:
        return math.factorial(x)


def sine(x):
    return math.sin(math.radians(x))


def cosine(x):
    return math.cos(math.radians(x))


def tangent(x):
    return math.tan(math.radians(x))


def menu():
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. Logarithm")
    print("8. Factorial")
    print("9. Sine")
    print("10. Cosine")
    print("11. Tangent")
    print("12. Exit")


while True:
    menu()
    choice = input("Enter choice(1/2/3/4/5/6/7/8/9/10/11/12): ")

    if choice == '12':
        print("Exiting the program.")
        break

    if choice in ['1', '2', '3', '4', '5']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
        elif choice == '5':
            print("Result:", power(num1, num2))

    elif choice == '6':
        num = float(input("Enter number: "))
        print("Result:", square_root(num))

    elif choice == '7':
        num = float(input("Enter number: "))
        base = float(input("Enter base: "))
        print("Result:", logarithm(num, base))

    elif choice == '8':
        num = int(input("Enter number: "))
        print("Result:", factorial(num))

    elif choice == '9':
        num = float(input("Enter angle in degrees: "))
        print("Result:", sine(num))

    elif choice == '10':
        num = float(input("Enter angle in degrees: "))
        print("Result:", cosine(num))

    elif choice == '11':
        num = float(input("Enter angle in degrees: "))
        print("Result:", tangent(num))

    else:
        print("Invalid input!")
