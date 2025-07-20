# Напишите код, который принимает список слов и возвращает новый список,
# отсортированный по возрастанию количества уникальных букв в словах.
# Используйте функцию sorted и ключ сортировки.

somewords = ['asa', 'adfda', 'qerraaaaeq', 'kjkj', 'kkoopp']

def uniqueletters(text):
    new_list = []
    for letter in text:
        if letter not in new_list:
            new_list += letter
    return sum(1 for x in text if x in new_list)

print(sorted(somewords, key=uniqueletters))