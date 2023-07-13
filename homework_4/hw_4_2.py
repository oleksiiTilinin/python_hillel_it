import random

LIST_SIZE = 10

try:
    numbers = []
    for i in range(LIST_SIZE):
        numbers.append(random.randint(1, 10))
    print(numbers)
    print(" --------------------------------")
    # Створити список цілих, що містить лише парні числа з першого списку;
    pair_list = []
    for i in numbers:
        if i % 2 == 0:
            pair_list.append(i)
    print("A list of integers containing only even numbers from the first list: ", pair_list, "\n",
          "--------------------------------")

    # Створити список цілих, що містить лише непарні числа з першого списку;
    unpaired_list = []
    for i in numbers:
        if i % 2 != 0:
            unpaired_list.append(i)
    print("A list of integers containing only odd numbers from the first list:", unpaired_list, "\n",
          "--------------------------------")

    # Створити список цілих, що містить лише негативні числа з першого списку;
    negative_list = []
    for i in numbers:
        if i < 0:
            negative_list.append(i)
    if negative_list:
        print("A list of integers containing only negative numbers from the first list:", negative_list, "\n",
              "--------------------------------")
    else:
        print("There is no negative numbers found in the first list.", "\n",
              "--------------------------------")

    # Створити список цілих, що містить лише позитивні числа з першого списку.
    positive_list = []
    for i in numbers:
        if i > 0:
            positive_list.append(i)
    if positive_list:
        print("A list of integers containing only positive numbers from the first list:", positive_list, "\n",
              "--------------------------------")
    else:
        print("There is no positive numbers found in the first list.", "\n",
              "--------------------------------")

except Exception as e:
    print(e)
