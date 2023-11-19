import os
from operator import itemgetter

path = "./example10-3.txt"
if not os.path.isfile(path) or not os.path.exists(path):
    print("файла нет")
    exit()

with open(path, "r") as f:
    people = f.readlines()

lib = list(map(lambda x: x.split(), people))
surname = sorted(lib, key=itemgetter(0))
age = sorted(lib, key=itemgetter(1), reverse=True)
print("от А-Я", *surname, "\n", "от младших к старшим", *age, sep="\n")
