num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")


if operation == "+":
    result = num1 + num2
    print(f"The result is: {result}")
elif operation == "-":
    result = num1 - num2
    print(f"The result is: {result}")
elif operation == "*":
    result = num1 * num2
    print(f"The result is: {result}")
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"The result is: {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation.")# Simple Calculator with Match-Case (Python 3.10+)