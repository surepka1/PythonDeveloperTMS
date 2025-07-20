# Задание 2.
# Напишите функцию, которая принимает на вход строку и заменяет в ней все множественные пробелы на одинарные.
#       Например: 'Hello,    world' -> 'Hello, world'
def replace_multiple_spaces(text):
    new_text = text.split()
    new_text = ' '.join(new_text)
    return print(new_text)
text = input()
replace_multiple_spaces(text)