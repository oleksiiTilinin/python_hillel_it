quantity_of_meters = int(input("Enter quantity of meters\n"))

choice = int(input("Choose option (1 - meters -> miles, 2 - meters -> inches, 3 - meters -> yards): "))

if choice == 1:
    print(int(quantity_of_meters * 0.00062137))
if choice == 2:
    print(int(quantity_of_meters * 39.370))
if choice == 3:
    print(int(quantity_of_meters * 1.0936))
else:
    print("Invalid choice, please try again")
