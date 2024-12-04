my_info = {
    "name": "Maksym",
    "age": 16,
    "details": {
        "hobby": "jiujitsu",
        "favorite_language": "Ukraine-English",
        "experience_years": 1,
        "city": "Lutsk",
        "sport": "jiujitsu"
    },
    "profession": "computer engineer"
}

print(my_info)

myinfo_types = {}
# Проходимо по ключам та значенням my_info
for key, val in my_info.items():  
    if isinstance(val, dict):  # Якщо значення — словник
        for sub_key, sub_val in val.items():  # Проходимо по вкладеному словнику
            myinfo_types[sub_key] = type(sub_val)  # Додаємо тип вкладених значень
    else:
        myinfo_types[key] = type(val)  # Якщо значення просте, додаємо його тип

print(myinfo_types)
