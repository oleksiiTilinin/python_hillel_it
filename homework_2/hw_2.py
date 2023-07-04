try:
    first_int = int(input("Enter first number: "))
    second_int = int(input("Enter second number: "))

    if first_int > second_int:
        print("first number", first_int, "is greater than", "second number", second_int)
    elif first_int < second_int:
        print("second number", second_int, "is greater than", "first number", first_int)
    else:
        print(first_int, "is equal to", second_int)
except ValueError:
    print("Incorrect input. Enter a number.")
