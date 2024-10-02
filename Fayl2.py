
with open("data.txt", 'r') as file:
    for count in file:
        print(len(count.strip()))

