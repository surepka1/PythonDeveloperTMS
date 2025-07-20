# Напишите код, который принимает список слов и возвращает новый список,
# отсортированный по возрастанию количества гласных букв в словах.
# Используйте функцию sorted и ключ сортировки.
# Для подсчета гласных букв
# используем встроенную функцию sum.

somewords = ['asa', 'adfda', 'qerreq', 'kjkj', 'kkoopp']

def vowelcount(text):
    vowels = 'EeYyUuOoAa'
    return sum(1 for x in text if x in vowels)

print(sorted(somewords, key=vowelcount))