import os
import re

path = "./data/ex9.4-in.txt"
if not os.path.exists(path):
    print("Файла не существует!")
    exit()

with open(path, "r") as f:
    strings = f.readlines()

with open("./data/9.4output.txt", "w") as f:
    for i in range(len(strings)):
        if re.match(r"Chapter*", strings[i]):
            f.write(strings[i] + strings[i + 1])
path2 = "./data/9.4output.txt"
with open(path2, "r") as f:
    print(*f.readlines(), sep="")
