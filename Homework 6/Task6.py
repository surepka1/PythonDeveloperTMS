# Задание 6.
# Напишите функцию, которая принимает на вход строку и возвращает новую строку,
# в которой все гласные буквы заменены на символ '*'.
def replace_vowels(text):
    vowels = 'aeiouAEIOUаеёиоуыэюяАЕЁИОУЫЭЮЯ'
    result_text = ''
    for letter in text:
        if letter in vowels:
            result_text += '*'
        else:
           result_text += letter
    return result_text


print(replace_vowels(input()))