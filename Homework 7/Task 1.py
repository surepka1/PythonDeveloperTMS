# Напишите код, который принимает список чисел и возвращает новый список,
# содержащий только четные числа из исходного списка. Используйте функцию
# filter и лямбда-выражение.
sequence = input()
sequence = sequence.split()
sequence = list(map(int, sequence))
result = list(filter(lambda x: x % 2 == 0, sequence))
print(result)
