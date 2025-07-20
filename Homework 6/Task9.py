# Задание 9.
# Напишите функцию, которая принимает на вход три целых числа и возвращает True,
# если они могут быть длинами сторон треугольника.
#       Подсказка: сумма двух сторон треугольника должна быть больше третьей стороны.
def is_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False
print(is_triangle(int(input()), int(input()), int(input())))