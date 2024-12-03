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

for key in my_info:
    val = my_info[key]
    if type(val) == my_info:
        for sub_key in val:
            sub_val = val[sub_key]  
            myinfo_types[sub_key] = type(sub_val)  
    else:
        myinfo_types[key] = type(val)
print(myinfo_types)
