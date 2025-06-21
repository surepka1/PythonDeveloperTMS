# Задание 1
# Через цикл вывести в консоль все элементы списка.
# Используя цикл, вывести в консоль все элементы списка в обратном порядке.
# Используя цикл, вывести в консоль все элементы списка, а их буквы в обратном порядке.
list1 = ['apple', 'banana', 'cherry']

last_index = len(list1) - 1  # 11

i = last_index
while i >= 0:
    print(list1[i])
    i -= 1  # i = i - 1

for i in range(last_index, -1, -1):
    print(list1[i])

for letter in list1[ : :-1]:
    print(letter)