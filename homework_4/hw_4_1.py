import random

NUMS_SIZE = 10

negative_sum = 0
even_sum = 0
odd_sum = 0
index_sum = 1

try:
    numbers = []
    for i in range(NUMS_SIZE):
        numbers.append(random.randint(1, 10))
    print(numbers)
    print(" --------------------------------")
    # Суму негативних чисел;
    for i in numbers:
        if i < 0:
            negative_sum += i
    print("The sum of negative numbers is:", negative_sum, "\n", "--------------------------------")

    # Суму парних чисел
    for i in numbers:
        if i % 2 == 0:
            even_sum += i
    print("The sum of paired numbers is:", even_sum, "\n", "--------------------------------")

    # Суму непарних чисел;
    for i in numbers:
        if i % 2 != 0:
            odd_sum += i
    print("The sum of unpaired numbers is:", odd_sum, "\n", "--------------------------------")

    # Добуток елементів з кратними індексами 3;
    for i in range(0, len(numbers), 3):
        index_sum *= numbers[i]
    print("Product of elements with multiple indices 3 is:", index_sum, "\n", "--------------------------------")

    # Добуток елементів між мінімальним та максимальним елементом;
    min_index = numbers.index(min(numbers))
    max_index = numbers.index(max(numbers))

    if min_index < max_index:
        start_index = min_index
        end_index = max_index
    else:
        start_index = max_index
        end_index = min_index

    product = 1
    for i in range(start_index + 1, end_index):
        product *= numbers[i]

    print("The product of elements between the minimum and maximum element is:", product, "\n",
          "--------------------------------")

    # Суму елементів, що знаходяться між першим та останнім позитивними елементами.
    # Find the index of the first positive element
    first_positive_index = -1
    for i, num in enumerate(numbers):
        if num > 0:
            first_positive_index = i
            break

    # Find the index of the last positive element
    last_positive_index = -1
    for i in range(len(numbers) - 1, -1, -1):
        if numbers[i] > 0:
            last_positive_index = i
            break

    # Calculate the sum of elements between the first and last positive elements
    sum_between = 0
    if first_positive_index != -1 and last_positive_index != -1:
        start_index = first_positive_index + 1
        end_index = last_positive_index
        sum_between = sum(numbers[start_index:end_index])

    print("The sum of the elements between the first and last positive elements is:", sum_between, "\n",
          "--------------------------------")










except Exception as e:
    print(e)
