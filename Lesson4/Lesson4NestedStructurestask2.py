# Задание 2

# Имеется структура данных продукта.

# Уменьшите цену товара на 10%.
# Уменьшите количество единиц товара черного цвета на 7 (не забудьте пересчитать общее количество единиц).
# Добавьте изображение товара.
# Добавьте review для товара с рейтингом 2.
# Пересчитайте среднюю оценку товара и количество отзывов.

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
        "quantity": 50
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
            "price": 199.99,
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

product1["price"] = product1["price"] * 0.9
print("Новая цена:" , product1["price"]) # Уменьшение цены товара на 10%.

product1["variants"][0]["stockQuantity"] = 7
print("blackStockQuantity:" , product1["variants"][0]["stockQuantity"])  # Уменьшение количества ед. товара черного цвета на 7.
print("totalStockQuantity:" , product1["variants"][0]["stockQuantity"] + # Общее количество ед. товара.
                              product1["variants"][1]["stockQuantity"]
      )

product1["images"].append("https://example.com/products/1001/side2.jpg") # Добавление изображения в конец списка.
print("addedImageLink" , product1["images"][-1]) # Вывод ссылки на изображение.

product1["reviews"].append( {
            "reviewId": 503,
            "userId": 103,
            "username": "teachmeskills",
            "rating": 2,
            "comment": "Bad sound quality and battery life!"
        }
)
print("addedReview:" , product1["reviews"][-1]) # Добавление отзыва на товар.

reviews = product1["reviews"] # Создание списка на основе вложенного словаря reviews.
product1["ratings"]["numberOfReviews"] = len(reviews) # Подсчет кол-ва элементов в словаре reviews.
print("Количество отзывов:" , product1["ratings"]["numberOfReviews"])
product1["ratings"]["averageRating"] = ( (reviews[0]["rating"] + # Сумма значений rating
                                          reviews[1]["rating"] + # каждого из элемпентов.
                                          reviews[2]["rating"])
                                        / len(reviews)
                                        )
print("Средняя оценка:" , product1["ratings"]["averageRating"])
