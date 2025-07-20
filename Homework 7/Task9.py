# Напишите функцию, которая принимает список строк и возвращает новый
# список, содержащий только те строки, которые являются палиндромами.
# Палиндром — это слово, которое читается одинаково слева направо и справа
# налево. Используйте функцию filter и сравнение строк.

somestrings = ['asa', 'adfda', 'qerreq', 'kjkj', 'kkoopp']

def is_palindrome(text):
    text = text.lower() # заглавные буквы => строчные
    text = text.split()
    text = ''.join(text) # удаление пробелов
    reversed_text = text[::-1]
    return text == reversed_text

print(list(filter(is_palindrome, somestrings)))
