# СПИСКИ
# 1. Создать произвольный список
# 2. Добавить новый элемент типа str в конец списка
# 3. Добавить новый элемент типа int на место с индексом
# 4. Добавить новый элемент типа list в конец списка
# 5. Добавить новый элемент типа tuple на место с
# индексом
# 6. Получить элемент по индексу
# 7. Удалить элемент

user_input = input()
user_list = list(user_input)                              # Создание списка из введенной строки.
print("Исходный список:" , user_list)
print("Новый элемент типа str для добавления:")
user_input2 = input()
user_list.append(user_input2)
print("Новый список с элементом типа str:" , user_list)
print("Новый элемент типа int для добавления:")
user_input3 = int(input())
print("Индекс элемента типа int:")
user_input4 = int(input())
user_list.insert(user_input4 , user_input3)
print("Новый список с элементом типа int:" , user_list)
print("Новый элемент типа list для добавления:")
user_input5 = list(input())                                # Преобразование элемента из типа str в list.
user_list.append(user_input5)
print("Новый список с элементом типа list:" , user_list)
print("Новый элемент типа tuple для добавления:")
user_input6 = tuple(input())                               # Преобразование элемента из типа str в tuple.
print("Индекс элемента типа tuple:")
user_input7 = int(input())
user_list.insert(user_input7 , user_input6)
print("Новый список с элементом типа tuple:" , user_list)
print("Введите индекс элемента на удаление:")
user_input8 = int(input())
print("Выбранный элемент:" , user_list.pop(user_input8))
print("Новый список без элемента:" , user_list)
