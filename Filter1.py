shaxslar = [
    {"ism": "Ali", "yosh": 17},
    {"ism": "Vali", "yosh": 22},
    {"ism": "Hasan", "yosh": 30},
    {"ism": "Husan", "yosh": 16}
]
natija=list(filter(lambda shaxs: shaxs['yosh']>18,shaxslar))
print(natija)