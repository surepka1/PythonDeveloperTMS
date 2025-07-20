# Задание 5
# На вход пользователь должен ввести username, email, имя и фамилию по очереди (использовать функцию input).
# Для каждого параметра: если введенные данные не соответствуют требованиям
# (например, username должен быть длиной от 3 до 20 символов),
# выведите сообщение об ошибке и попросите ввести данные заново.
# Создайте словарь с данными пользователя и выведите его в консоль.
print('username:')
username = input()
print('email:')
email = input()
print('имя:')
name = input()
print('фамилия:')
surname = input()


while len(username) <= 3 or len(username) >= 20:
    print('username должен быть длиной от 3 до 20 символов, введите заново:')
    username = input()

while '@' not in email:
    print('email должен содержать "@", введите заново:')
    email = input()

keys = ['username', 'email','имя', 'фамилия']
values = [username, email, name, surname]
new_dict = dict(zip(keys, values))
print(new_dict)

