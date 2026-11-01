#Let's build a python calculator 

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(add(num1, num2))