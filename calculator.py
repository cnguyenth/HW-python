def calculator(number1, number2, operator):
    if operator == "+":
        print(number1 + number2)
        return True
    elif operator == "-":
        print(number1 - number2)
        return True
    elif operator == "*":
        print(number1 * number2)
        return True
    elif operator == "/":
        print(number1 / number2)
        return True
    elif operator == "//":
        print(number1 // number2)
        return True
    elif operator == "**":
        print(number1 ** number2)
        return True
    else:
        return False

def input_output():
    cont = True

    while cont:
        number1 = input("Enter the first number: ")
        number2 = input("Enter the second number: ")
        operation = input("Enter the operation: ")
        
        number1 = float(number1)
        number2 = float(number2)

        cont = calculator(number1, number2, operation)
        if cont:
            userAnswer = input("Do you wish to exit?")
            if userAnswer == "y":
                cont = False

