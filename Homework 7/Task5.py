# Напишите код, который принимает список слов и возвращает новый список,
# отсортированный по убыванию длины слов. Используйте функцию sorted и
# обратный порядок сортировки.
word_list = ['apple', 'banana', 'cherry','pineapple']
print(sorted(word_list, key = lambda x: len(x), reverse = True))