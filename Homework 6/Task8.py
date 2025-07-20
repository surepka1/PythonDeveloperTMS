# Задание 8.
# Напишите функцию, которая принимает на вход число и возвращает True,
# если число является степенью двойки, и False - в противном случае.
#       Например: 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536 и т.д.
#       Подсказка: используйте цикл и оператор деления без остатка.
from logging import exception


def is_power_of_two(number):
    if number < 1:
        return False
    while number > 1:
        if number % 2 != 0:
            return False
        number = number // 2
    return True # выход из цикла

print(is_power_of_two(int(input())))
