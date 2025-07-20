# Напишите код, который принимает список строк и возвращает новый список,
# содержащий только те строки, которые начинаются с гласной буквы. (Да да,
# снова эти гласные) Используйте функцию filter и множество.
list1 = ['isss', 'dadd', 'ow', 'www', 'dwwdow', 'uqswdd', 'eff']
listwithvowels = {x for x in list1 if x[0] in 'EeYyUuOoAa'}
print(listwithvowels)

