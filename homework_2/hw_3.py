try:
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    operator = input("Enter the math operation (+, -, *, /): ")

    result = None

    if operator == "+":
        result = number1 + number2
    elif operator == "-":
        result = number1 - number2
    elif operator == "*":
        result = number1 * number2
    elif operator == "/":
        if number2 != 0:
            result = number1 / number2
        else:
            print("Error: Division by zero!")
    else:
        print("Invalid math operation.")

    if result is not None:
        print("Result:", result)

except ValueError:
    print("Invalid input. Enter numbers.")
