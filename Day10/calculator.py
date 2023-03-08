# my little calculator

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculator(): # start learning about recursion - function calling itself
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True
    
    while should_continue:
        operation_symbol = input("Pick an operation from above: ")
        num2 = float(input("What is the second number: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        more_calculations = input(f"Type 'y' to continue calculating with {answer}, 'n' to start a new calculation, or 'e' to exit: ")
        
        if more_calculations == 'y':
            num1 = answer
        elif more_calculations == 'n':
            calculator() # recursive call
        elif more_calculations == 'e':
            should_continue = False
            
        
calculator()