# Завдання 1.
# Написати рекурсивну функцію знаходження ступеня числа.
def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent - 1)


# Завдання 2.
# Написати рекурсивну функцію, яка виводить N зірок у ряд, число N задає користувач.
# Проілюструйте роботу функції прикладом. (Протестувати)
def print_stars(n):
    if n <= 0:
        return
    print('*', end='')
    print_stars(n - 1)


# Example of usage:
num_stars = int(input("Input the quantity of the stars (integer): "))
print_stars(num_stars)


# Завдання 3.
# Написати рекурсивну функцію, яка обчислює суму всіх чисел у діапазоні від a до b.
# Користувач вводить a та b. Проілюструйте роботу функції прикладом.

def sum_range(a, b):
    if a > b:
        return 0
    else:
        return a + sum_range(a + 1, b)


# Example of usage:
start_num = int(input("Enter the starting number (integer): "))
end_num = int(input("Enter the ending number (integer): "))
result = sum_range(start_num, end_num)
print(f"The sum of numbers in the range from {start_num} to {end_num} is {result}")
