# Напишите код, который принимает список строк и возвращает новый список,
# содержащий эти же строки с добавленным префиксом “Hello”. Используйте
# функцию map и конкатенацию строк.

somestrings = ['asa', 'adfda', 'qerreq', 'kjkj', 'kkoopp']

print(list(map(lambda x: 'Hello ' + x, somestrings)))