# СЛОВАРИ
# 1. Создать произвольный словарь
# 2. Добавить новый элемент с ключом типа str и значением
# типа int
# 3. Добавить новый элемент с ключом типа кортеж(tuple) и
# значением типа список(list)
# 4. Получить элемент по ключу
# 5. Удалить элемент по ключу

fr = {
    "name": "France",
    "capital": "Paris",
    "population": 67364357,
    "area": 551695,
    "currency": "Euro",
    "languages": ["French"],
    "region": "Europe",
    "subregion": "Western Europe",
    "flag": "https://upload.wikimedia.org/wikipedia/commons/c/c3/Flag_of_France.svg"
}
fr["Barcode"] = int(300) # Добавление нового элемента с ключом типа str и значением типа int
print(fr)
fr[("Month" , "Date")] = ["9th November 1799" , "28th May 1794"]  # Добавление нового элемента с ключом типа типа кортеж(tuple) и значением типа список(list)
print(fr)
print(fr.get("region"))
fr.pop("region")
print(fr)
