# Задание 2
# Используя цикл, вывести в консоль все ключи словаря.
# Используя цикл, вывести в консоль все ключи и значения словаря.
dict1 = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

for key in dict1.keys():
    print(key)

for key, value in dict1.items():
    print(key, value)
