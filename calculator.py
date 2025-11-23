# calculator.py

import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

def power(a, b):
    return a ** b

def sqrt(a):
    if a < 0:
        return "Error: Cannot take square root of negative number"
    return math.sqrt(a)

def log(a):
    if a <= 0:
        return "Error: Log undefined for zero or negative numbers"
    return math.log(a)

def sin(a):
    return math.sin(math.radians(a))

def cos(a):
    return math.cos(math.radians(a))

def tan(a):
    return math.tan(math.radians(a))

def factorial(a):
    if a < 0:
        return "Error: Factorial undefined for negative numbers"
    return math.factorial(int(a))
