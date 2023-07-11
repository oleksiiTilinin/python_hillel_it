import string

try:
    new_str = "lorem ipsum dolor sit amet, consectetur adipiscing"

    # 1 - Спершу виведіть третій символ цього рядка.
    print("Third character of this string is: " + new_str[3] + "\n")

    # 2 - У другому рядку виведіть передостанній символ цього рядка.
    print("The penultimate character of this string: " + new_str[-2] + "\n")

    # 3 - У третьому рядку виведіть перші п'ять символів цього рядка.
    print("The first five characters of this string: " + new_str[0:5] + "\n")

    # 4 - У четвертому рядку виведіть весь рядок, крім двох останніх символів.
    print("The entire string except the last two characters.: " + new_str[0:-2] + "\n")

    # 5 - У п'ятому рядку виведіть усі символи з парними індексами (вважаючи, що індексація починається з 0, тому символи виводяться з першого).
    print("All characters with even indices: " + new_str[::2] + "\n")

    # 6 - У шостому рядку виведіть усі символи з непарними індексами, тобто, починаючи з другого символу рядка.
    print("All the characters with odd indexes: " + new_str[1::2] + "\n")

    # 7 - У сьомому рядку виведіть усі символи у зворотному порядку.
    print("All the characters in reverse order: " + new_str[::-1] + "\n")

    # 8 - У восьмому рядку виведіть усі символи рядка через один у зворотному порядку, починаючи з останнього.
    print("All the characters in the string in reverse order, starting with the last one: " + new_str[::-2] + "\n")

    # 9 - У дев'ятому рядку виведіть довжину цього рядка.
    print("The length of the string is: " + str(new_str.__len__()))

except Exception as e:
    print(e)
