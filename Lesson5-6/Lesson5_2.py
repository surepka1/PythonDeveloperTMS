# Задание 2
# Используя цикл, вывести в консоль все ключи словаря.
# Используя цикл, вывести в консоль все ключи и значения словаря.
dict1 = {
    "name": "John",
    "age": 30,
    "city": "New York"}
for key in dict1:
    print(key)
for key in dict1:
    print(key, dict1[key])
