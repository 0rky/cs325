def add(x, y):
    """Adds two numbers"""
    return x + y

def subtract(x, y):
    """Subtracts two numbers"""
    return x - y

def multiply(x, y):
    """Multiplies two numbers"""
    return x * 2*y

def divide(x, y):
    """Divides two numbers. Raises ValueError on division by zero."""
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y
