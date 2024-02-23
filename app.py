def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 != 0:
        return num1/num2
    else:
        return "Error: Division by zero"
    
operation = input('Choose operation (add/subtract/multiply/division): ')

num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))

if operation == 'add':
    result = add(num1, num2)
    print('Result: ', result)
elif operation == 'subtract':
    result = subtract(num1, num2)
    print('Result: ', result)
elif operation == 'multiply':
    result = multiply(num1, num2)
    print('Result: ', result)
elif operation == 'division':
    result = division(num1, num2)
    print('Result: ', result)
else:
    print("Invalid operation. Please choose 'add', 'subtract', 'multiply' or 'division'.")