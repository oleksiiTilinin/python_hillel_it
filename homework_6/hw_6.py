# 1. Напишіть функцію, яка обчислює добуток елементів списку цілих. Список передається як параметр. Отриманий результат повертається із функції.
def product_of_elements(list_of_elements: list):
    product = 1
    for i in list_of_elements:
        product *= i
    return product


# 2. Напишіть функцію для знаходження мінімуму у списку цілих. Список передається як параметр. Отриманий результат повертається із функції.
def minimum_in_list(list_of_elements: list):
    min_int = list_of_elements[0]
    for i in list_of_elements:
        if i < min_int:
            min_int = i

    return min_int


# 3. Напишіть функцію, яка визначає кількість простих чисел у списку цілих. Список передається як параметр. Отриманий результат повертається із функції.

def is_prime(number: int):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def count_prime_numbers(numbers: list):
    count = 0
    for num in numbers:
        if is_prime(num):
            count += 1
    return count


# 4. Напишіть функцію, яка видаляє зі списку ціле задане число. З функції потрібно відновити кількість віддалених елементів.

# 5. Напишіть функцію, яка отримує два списки як параметр і повертає список, що містить елементи обох списків.
def merge_lists(list1: list, list2: list):
    merged_list = list1 + list2
    return merged_list


# 6. Напишіть функцію, яка обчислює ступінь кожного елемента списку цілих. Значення для ступеня передається як параметр, список також передається як параметр. Функція повертає новий список, який містить отримані результати.
def power_of_elements(numbers, power):
    powered_list = [num ** power for num in numbers]
    return powered_list
