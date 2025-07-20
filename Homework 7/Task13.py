# Напишите код, который принимает список слов и возвращает новый список,
# отсортированный по возрастанию количества букв “a” в словах. Используйте
# функцию sorted и ключ сортировки.

somewords = ['asa', 'adfda', 'qerraaaaeq', 'kjkj', 'kkoopp']

def a_count(text):
    a = 'Aa'
    return sum(1 for x in text if x in a)

print(sorted(somewords, key=a_count))