def get_number(prompt):
    while True:
        user_input = input(prompt)
        if user_input.lower() in ('q', 'quit'):
            print("Exiting calculator. Goodbye!")
            exit()
        try:
            return float(user_input)
        except ValueError:
            print("Error: Please enter a valid number.")

def get_operation():
    allowed_operations = ['+', '-', '*', '/', '**', '%']
    while True:
        op = input("Enter operation (+, -, *, /, **, %): ")
        if op.lower() in ('q', 'quit'):
            print("Exiting calculator. Goodbye!")
            exit()
        if op in allowed_operations:
            return op
        else:
            print("Error: Invalid operation. Please choose a valid operation.")

def perform_operation(a, b, op):
    try:
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        elif op == '/':
            if b == 0:
                raise ZeroDivisionError
            return a / b
        elif op == '**':
            return a ** b
        elif op == '%':
            if b == 0:
                raise ZeroDivisionError
            return a % b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        return None

def calculator():
    print("Welcome to the Interactive Calculator!")
    print("Type 'q' or 'quit' at any prompt to exit.\n")
    
    while True:
        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")
        operation = get_operation()

        result = perform_operation(num1, num2, operation)
        if result is not None:
            print(f"Result: {num1} {operation} {num2} = {result}\n")

# Run the calculator
calculator()
