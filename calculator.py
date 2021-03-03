def calculator(number1, number2, operator):
    """
    Perform operations on two numbers.

    Add, subtract, multiply, divide, integer divide, or raise to a power two numbers. Return true if operation is valid and print the result. Return false if operation is invalid.

    Parameters
    ----------
    number1 : float
        First number in the operation.
    number2 : float
        Second number in the operation.
    operator : string
        Which operation to use.

    Returns
    -------
    bool
        If operation is valid or not.

    Examples
    --------
    >>> calculator(4.5, 2.5, "+")
    7.0
    True
    >>> calculator(10, 2, "/")
    5.0
    True

    """
    if operator == "+":
        return number1 + number2
    elif operator == "-":
        return number1 - number2
    elif operator == "*":
        return number1 * number2
    elif operator == "/":
        return number1 / number2
    elif operator == "//":
        return number1 // number2
    elif operator == "**":
        return number1 ** number2
    else:
        return False

def input_output():
    """
    Take input from user and call calculator function.

    Ask user to enter numbers and operation they want, call calculator function, then ask user if they want to continue

    Examples
    --------
    Enter the first number: 2
    Enter the second number: 5
    Enter the operation: **
    32.0
    Do you wish to exit? n
    Enter the first number: 1
    Enter the second number: 6
    Enter the operation: -
    -5.0
    Do you wish to exit? y
    """
    
    cont = True

    while cont:
        number1 = input("Enter the first number: ")
        number2 = input("Enter the second number: ")
        operation = input("Enter the operation: ")
        
        number1 = float(number1)
        number2 = float(number2)

        cont = calculator(number1, number2, operation)
        if isinstance(cont, int) or isinstance(cont, float):
            print(cont)
            userAnswer = input("Do you wish to exit? ")
            if userAnswer == "y":
                cont = False

