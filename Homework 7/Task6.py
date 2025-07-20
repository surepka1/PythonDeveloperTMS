# Напишите код, который принимает строку и возвращает список, содержащий
# только те буквы, которые встречаются в слове “python”. Используйте функцию
# filter и оператор in.
somestring = 'wxnejHdekdmelNdklwwPknewvlvwl'
print(list(filter(lambda x: x in 'PpYyTtHhOoNn', somestring)))