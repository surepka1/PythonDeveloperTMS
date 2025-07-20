# Напишите код, который принимает список строк и возвращает новый список,
# содержащий эти же строки в верхнем регистре. Используйте функцию map и
# встроенный метод строк upper

somestrings = ['asa', 'adfda', 'qerreq', 'kjkj', 'kkoopp']
print(list(map(lambda x: x.upper(), somestrings)))