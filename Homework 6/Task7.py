# Задание 7.
# Напишите функцию, которая принимает на вход число и возвращает сумму его цифр.

def sum_digits(numbers):
    i = 0
    for number in str(numbers):
        i += int(abs(number)) # убирается минус, строка преобразована в число
    return i

print(sum_digits(input()))