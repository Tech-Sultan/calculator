def multiplication(num1, num2):
    result = num1 * num2
    return int(result)


def subtraction(num1, num2):
    result = num1 - num2
    return int(result)


def addition(num1, num2):
    result = num1 + num2
    return int(result)


def division(num1, num2):
    result = num1 / num2
    return int(result)


if __name__ == "__main__":
    number1 = float(int(input('Please enter first number : ')))
    operation = input('Please enter operation: ')
    number2 = float(int(input('Please enter second number : ')))
    if operation == '*':
        res1 = multiplication(number1, number2)
        print('The result in multiplication is', res1)
    elif operation == '-':
        res2 = subtraction(number1, number2)
        print('The result in subtraction is', res2)
    elif operation == '+':
        res3 = addition(number1, number2)
        print('The result in addittion is', res3)
    elif operation == '/':
        res4 = division(number1, number2)
        print('The result in division is', res4)
    else:
        print('Enter correct operation. * or - or + or /')
