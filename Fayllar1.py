def ismlar_yozish(matn):
    with open("names.txt", 'w') as file:
        for ism in matn:
            file.write(ism+'\n')


matn= ["Ali", "Vali", "Hasan", "Husan"]
ismlar_yozish(matn)

