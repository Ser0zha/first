import os
import re


path = './data/ex9.2-in.txt'
if not os.path.exists(path):
    print("Файла нет")
    exit()

with open(path, "r") as f:
    pere = f.readline()
    if not pere:
        print("Пустой файл")
        exit()
    if pere.isdigit():
        print("Введины числа")
        exit()

sentence = re.split(r"[!?.]", pere)
try:
    value = int(input("Введите количество слов в предложении: "))
    if value < 0:
        print("Введено маленькое значние")
        exit()
except ValueError:
    print("Введино некорректное значние")
    exit()
s = ""
for i in sentence:
    if len(i.split()) > value:
        s += i
        with open("./data/9.2output.txt", "w") as f:
            f.write(s)
        print(i.strip())
