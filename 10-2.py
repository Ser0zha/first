import os

path = "./for10-2.txt"
if not os.path.isfile(path) or not os.path.exists(path):
    print("файла нет")
    exit()

with open(path, encoding='utf-8') as f:
    words = f.readlines()

words.sort(key=lambda x: x.count('а'))
words.reverse()
# или
# words.sort(reverse=True, key=lambda x: x.count('а'))
print(*words, sep='')
