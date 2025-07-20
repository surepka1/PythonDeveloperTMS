# Задание 5.
# Напишите функцию, которая принимает на вход строку и возвращает новую строку,
#       в которой все символы, которые не являются буквами, удалены (пробел разрешен).
#       Например: 'Hello, world!' -> 'Hello world'
#       Подсказка: используйте цикл и метод строки `isalpha()` для проверки, является ли символ буквой.
def remove_non_letters(text):
    result_text = ''
    for letter in text:
        if letter.isalpha() or letter == ' ':
            result_text += letter
    return result_text
print(remove_non_letters(input()))


