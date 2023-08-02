import re


# Написати валідації за допомогою регулярних виразів:
# - Мобільний номер телефону (тільки цифри, можлива наявність плюса, довжина номера)
def validate_mobile_number(phone_number):
    pattern = r'^\+?\d{10,15}$'
    return bool(re.match(pattern, phone_number))


# - домашній номер телефону (тільки цифри та довжина номера)

def validate_home_number(phone_number):
    pattern = r'^\d{7,10}$'
    return bool(re.match(pattern, phone_number))


# - email (наявність @, домену: gmail.com наприклад, мінімальна довжина та максимальна на ваш вибір)

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


# - ПІБ клієнта (3 слова, мінімальна довжина 2 символи, максимальна довжина 20)
def validate_full_name(full_name):
    pattern = r'^[a-zA-Zа-яА-Я]{2,20}(?:\s[a-zA-Zа-яА-Я]{2,20}){2}$'
    return bool(re.match(pattern, full_name))


# додатково:
# - Пароль (мінімально: одна велика літера, одна маленька літера, одна цифра, один символ, довжина пароля – від 8 до 16 символів)
def validate_password(password):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,16}$'
    return bool(re.match(pattern, password))


# Example of using
mobile_number = "+380987654321"
home_number = "0441234567"
email = "example@gmail.com"
full_name = "John Doe Smith"
password = "StrongP@ss123"

print(validate_mobile_number(mobile_number))
print(validate_home_number(home_number))
print(validate_email(email))
print(validate_full_name(full_name))
print(validate_password(password))
