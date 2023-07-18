try:
    numbers = [2, 2, 2, 3, 3, 5, 8, 1, 4]
    # 1. Створити список чисел. Заберіть дублікати значень. Вивести унікальні значення.
    res = [*set(numbers)]
    print(numbers)
    print("List after removing duplicate elements: ", res, "\n",
          "--------------------------------")

    # 2. Дано два списки чисел. Порахуйте, скільки чисел міститься як у першому списку, і у другому.
    first_list = [1, 2, 4, 5, 6]
    second_list = [2, 3, 3, 4, 5, 6]

    common_elements_first = len(set(first_list).intersection(second_list))
    common_elements_second = len(set(second_list).intersection(first_list))

    print(first_list)
    print(second_list)

    print("Number of common elements in the first list:", common_elements_first)
    print("Number of common elements in the second list:", common_elements_second, "\n",
          "--------------------------------")

    #     3. Даний текст: у першому рядку записано число рядків, далі йдуть самі рядки. Визначте, скільки різних слів міститься у цьому тексті.
    num_lines = int(input("Input raw quantity: "))
    unique_words = set()

    for i in range(num_lines):
        line = input()
        words = line.split()
        unique_words.update(words)

    unique_word_count = len(unique_words)

    print("The quantity of unique words is :", unique_word_count)

except ValueError as v:
    print("Oops! That's is not a valid number. Please enter a quantity of the raw and try again...")
except Exception as e:
    print(e)
