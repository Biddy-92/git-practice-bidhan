def add(a, b):
    try:
        return a + b
    except TypeError:
        return "Error: Invalid input type"

def subtract(a, b):
    try:
        return a - b
    except TypeError:
        return "Error: Invalid input type"

def multiply(a, b):
    try:
        return a * b
    except TypeError:
        return "Error: Invalid input type"
    

def divide(a, b):
    try:
        return a / b
    except TypeError:
        return "Error: Invalid input type"