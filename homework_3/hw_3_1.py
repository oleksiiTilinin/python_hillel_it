try:
    input_string = (input("Input string: "))
    letter_count = 0
    digit_count = 0

    for char in input_string:
        if char.isalpha():
            letter_count += 1
        elif char.isdigit():
            digit_count += 1

    print("The quantity of letter is :", letter_count)
    print("The quantity of number is ::", digit_count)
except Exception as e:
    print(e)
