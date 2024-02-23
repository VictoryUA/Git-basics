def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

operation = input('Choose operation (add/subtract/multiply/): ')
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
else:
    print("Invalid operation. Please choose 'add', 'subtract' or 'multiply'.")