import math

def addition(x, y):
    """
    Add two numbers.

    Args:
        x (int, float): The first number.
        y (int, float): The second number.

    Returns:
        int, float: The sum of x and y.
    """
    return x + y


def subtraction(x, y):
    """
    Subtract two numbers.

    Args:
        x (int, float): The first number.
        y (int, float): The second number.

    Returns:
        int, float: The difference of x and y.
    """
    return x - y


def multiplication(x, y):
    """
    Multiply two numbers.

    Args:
        x (int, float): The first number.
        y (int, float): The second number.

    Returns:
        int, float: The product of x and y.
    """
    return x * y


def division(x, y):
    """
    Divide two numbers.

    Args:
        x (int, float): The first number.
        y (int, float): The second number.

    Returns:
        int, float, str: The quotient of x and y, or an error message if x and y are not divisible.
    """
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

def square(x):
    """
    Square a number.

    Args:
        x (int): The number.

    Returns: int: The square of x.
    """
    return x * x

def root(x):
    """
    Root of a number.

    Args:
        x (int): The number.

    Returns: int: The root of x.
    """
    return math.sqrt(x)

def factorial(x):
    """
    Factorial of a number.

    Args:
        x (int): The number.

    Returns: int: The factorial of x.
    """
    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x - 1)