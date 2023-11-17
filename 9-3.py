import os

path = "./data/ex9.3-in.txt"
if not os.path.exists(path):
    print("Файла не существует!")
    exit()

with open(path, "r") as f:
    strings = f.readlines()

print(*strings, sep='')
