# Задание 8*

# Имеется структура данных продукта.

# Сейчас кол-во товара на складе равно 0. Посчитайте кол-во исходя из вариантов товара на складе.
# Выведите через цикл все варианты товара на складе в виде строки в формате: "Название - цена (кол-во на складе)".
# Используя цикл, найдите вариант товара с максимальной ценой и выведите его название и цену в консоль.
# Выведите через цикл все отзывы о товаре в виде строки в формате: "Пользователь - Оценка - Комментарий".
# Посчитайте через цикл количество отзывов с оценкой 5 и выведите их количество в консоль.
# Через цикл выведите только названия файлов картинок (например, "main.jpg" и "side.jpg") товара в консоль.
# Используя цикл, найдите и выведите в консоль все отзывы пользователя с именем "techguy123".

product1 = {
    "productId": 1001,
    "productName": "Wireless Headphones",
    "description": "Noise-cancelling wireless headphones with Bluetooth 5.0 and 20-hour battery life.",
    "brand": "SoundPro",
    "category": "Electronics",
    "price": 199.99,
    "currency": "USD",
    "stock": {
        "available": True,
        "quantity": 0
    },
    "images": [
        "https://example.com/products/1001/main.jpg",
        "https://example.com/products/1001/side.jpg"
    ],
    "variants": [
        {
            "variantId": "1001_01",
            "color": "Black",
            "price": 199.99,
            "stockQuantity": 20
        },
        {
            "variantId": "1001_02",
            "color": "White",
            "price": 198.99,
            "stockQuantity": 30
        }
    ],
    "dimensions": {
        "weight": "0.5kg",
        "width": "18cm",
        "height": "20cm",
        "depth": "8cm"
    },
    "ratings": {
        "averageRating": 4.7,
        "numberOfReviews": 2
    },
    "reviews": [
        {
            "reviewId": 501,
            "userId": 101,
            "username": "techguy123",
            "rating": 5,
            "comment": "Amazing sound quality and battery life!"
        },
        {
            "reviewId": 502,
            "userId": 102,
            "username": "jane_doe",
            "rating": 4,
            "comment": "Great headphones but a bit pricey."
        }
    ]
}

# Сейчас кол-во товара на складе равно 0. Посчитайте кол-во исходя из вариантов товара на складе.
amount = 0
for variant in product1["variants"]:
    amount += variant['stockQuantity']
print('Количество вариантов:', amount)

# Выведите через цикл все варианты товара на складе в виде строки в формате: "Название - цена (кол-во на складе)"
variants = product1['variants']
for variant in variants:
    print(product1['productName'], '-', variant['price'], f'({variant['stockQuantity']})')

# Используя цикл, найдите вариант товара с максимальной ценой и выведите его название и цену в консоль.
prices = []
for item in product1['variants']:
    prices.append(item['price']) # Все цены в одном списке.

targetValue = max(prices) # max цена

for item in product1['variants']:
        if targetValue in item.values():
            print('Товар с самой высокой ценой:', product1['productName'],
                  item['variantId'], item['price'])

# Выведите через цикл все отзывы о товаре в виде строки в формате: "Пользователь - Оценка - Комментарий".
reviews = product1['reviews']
for review in reviews:
    print(review['username'], review['rating'], review['comment'], sep = ' - ')

# Посчитайте через цикл количество отзывов с оценкой 5 и выведите их количество в консоль.
review_qty = 0
for item in product1['reviews']:
    if item['rating'] == 5:
        review_qty += 1
print('Количество отзывов с оценкой "5":', review_qty)
for item in product1['reviews']:
    if item['rating'] == 5:
        print('Отзывы с оценкой "5":', item)

# Через цикл выведите только названия файлов картинок (например, "main.jpg" и "side.jpg") товара в консоль.
for image in product1['images']:
    print(image[34:-1])

# Используя цикл, найдите и выведите в консоль все отзывы пользователя с именем "techguy123".
for review in product1['reviews']:
    if 'techguy123' in review.values():
        print(review)



