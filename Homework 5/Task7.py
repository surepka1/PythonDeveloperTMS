# Задание 7*
# Имеется структура данных пользователя.
# Используя цикл, выведите все активности по логам пользователя в консоль со временем и описанием.
# Если пользователь активен, выведите сообщение "Пользователь активен", иначе выведите "Пользователь не активен".
# Если у пользователя есть аватар, то выведите его в консоль, если нет, то выведите "Нет аватара".
user1 = {
    "userId": 2,
    "username": "janedoe",
    "email": "janedoe@example.com",
    "profile": {
        "firstName": "Jane",
        "lastName": "Doe",
        "birthDate": "1992-04-12",
        "gender": "female",
        "avatarUrl": "https://example.com/avatars/janedoe.jpg",
        "bio": "Digital marketer and blogger."
    },
    "accountStatus": {
        "isActive": True,
        "lastLogin": "2025-01-10T09:15:00Z",
        "createdAt": "2023-03-20T11:00:00Z"
    },
    "activityLogs": [
        {
            "timestamp": "2025-01-09T18:30:00Z",
            "activity": "Commented on a post"
        },
        {
            "timestamp": "2025-01-08T16:45:00Z",
            "activity": "Liked a post"
        }
    ]
}
# Используя цикл, выведите все активности по логам пользователя в консоль со временем и описанием.
for logs in user1["activityLogs"]:
    print(logs)

# Если пользователь активен, выведите сообщение "Пользователь активен", иначе выведите "Пользователь не активен".
if user1["accountStatus"]["isActive"] == True:
    print('Пользователь активен')
else:
    print('Пользователь неактивен')

# Если у пользователя есть аватар, то выведите его в консоль, если нет, то выведите "Нет аватара".
if not user1["profile"]["avatarUrl"]:
    print('Нет аватара')
else:
    print('Аватар:', user1["profile"]["avatarUrl"])
