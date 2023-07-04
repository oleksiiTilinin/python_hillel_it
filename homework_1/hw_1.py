num1 = int(input("Enter first number\n"))
num2 = int(input("Enter second number\n"))
num3 = int(input("Enter third number\n"))

choice = int(input("Choose option (1 - max, 2 - min, 3 - the arithmetic mean of the three numbers): "))

if choice == 1:
    maximum = int(max(num1, num2, num3))
    print("Max:", maximum)
elif choice == 2:
    minimum = int(min(num1, num2, num3))
    print("Min:", minimum)
elif choice == 3:
    average = int(num1 + num2 + num3) / 3
    print("the arithmetic mean:", average)
else:
    print("Wrong choice of the option, try again")
