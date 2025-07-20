# Напишите код, который принимает список чисел и возвращает новый список,
# содержащий эти же числа, умноженные на 10. Используйте функцию.

somelist = [1, 2, 3, 4, 5, 6, 7, 8]

def multiplyby10(numbers):
    result = []
    for num in numbers:
        result.append(num * 10)
    return result

print(multiplyby10(somelist))