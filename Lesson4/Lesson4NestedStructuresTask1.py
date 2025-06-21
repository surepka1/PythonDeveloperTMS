# Задание 1
from cProfile import Profile

# Имеется структура данных пользователя.

# Уменьшите день рождения пользователя на 1 день.
# Измените язык пользователя на "ru".
# Измените тему на "dark".
# Измените статус активности на "false".
# Добавьте новую запись в историю активности пользователя.

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
    "preferences": {
        "language": "fr",
        "theme": "light",
        "notifications": {
            "email": False,
            "sms": True,
            "push": True
        },
        "privacy": {
            "showOnlineStatus": True,
            "profileVisibility": "public"
        }
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
user1.get("birthDate")
user1 ["profile"]["birthDate"] = "1992-04-11"

user1 ["preferences"]["language"] = "ru"

user1 ["preferences"]["theme"] = "dark"

user1 ["accountStatus"]["isActive"] = False

user1["activityLogs"].append(
                              {"timestamp": "2025-03-09T16:47:00Z" ,
                              "activity": "Liked a post"}
                            )
print(user1)