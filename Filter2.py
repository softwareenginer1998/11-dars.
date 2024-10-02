mahsulotlar = [
    {"nomi": "Mahsulot1", "narx": 45},
    {"nomi": "Mahsulot2", "narx": 55},
    {"nomi": "Mahsulot3", "narx": 30},
    {"nomi": "Mahsulot4", "narx": 70}
]
natija=list(filter(lambda mahsulot : mahsulot['narx']<50, mahsulotlar))
print(natija)