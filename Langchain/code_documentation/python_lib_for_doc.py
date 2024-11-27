def add(a, b):
    """Description:
         Adds two numbers.
Arguments:
        a (int or float): The first number.
        b (int or float): The second number.
Response:
        int or float: The sum of the two numbers."""
    return a + b


def substract(a, b):
    """Description:
     Subtracts two numbers.
Arguments:
    a (int or float): The first number.
    b (int or float): The second number.
Response:
    int or float: The difference between the two numbers."""
    if a > b:
        return a - b
    return b - a


def multiply(a, b):
    """Description:
         Multiplies two numbers.
Arguments:
        a (int or float): The first number.
        b (int or float): The second number.
Response:
        int or float: The product of the two numbers."""
    return a * b


def solve(a, b):
    """Description:
    Performs arithmetic operations on two numbers.
Arguments:
    a (int or float): The first number.
    b (int or float): The second number.
Response:
    int or float: The product of the addition and subtraction of the two numbers."""
    print('Numbers are {} and {}'.format(a, b))
    add_res = add(a, b)
    sub_res = substract(a, b)
    return add_res * sub_res
