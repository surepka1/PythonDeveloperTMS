# Задание 10.
# Напишите функцию, которая принимает на вход строку и возвращает новую строку, в которой все символы,
# которые встречаются более одного раза, заменены на символ '_'.
def replace_duplicates(text):
    result_text = ''
    for letter in text:
        if text.count(letter) > 1:
            result_text += '_'
        else:
            result_text += letter
    return result_text

print(replace_duplicates(input()))