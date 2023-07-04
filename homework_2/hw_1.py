try:
    day_number = int(input("Input number of the day of the week (1-7): "))

    match day_number:
        case 1:
            print("Monday")
        case 2:
            print("Tuesday")
        case 3:
            print("Wednesday")
        case 4:
            print("Thursday")
        case 5:
            print("Friday")
        case 6:
            print("Saturday")
        case 7:
            print("Sunday")
        case _:
            print("Incorrect number, please input number in range from 1 to 7.")
except ValueError:
    print("Incorrect input. Enter a number.")
