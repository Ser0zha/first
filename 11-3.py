import  os

path = "./queue.txt"
with open(path, "r") as f:
    d = [[n for n in string.replace(",", "").split()] for string in f.readlines()]
    if not d:
        print("Пустой файл")
        exit()

if os.path.splitext(path)[-1] != ".txt":
        print("Входной файл должен иметь формат txt")
        exit()
if not os.path.exists(path) or not os.path.isfile(path):
    print("файла нет")
    exit()
res = ""
while any(map(lambda x: len(x), d)):
   for queue in d:
       if len(queue):
           res += queue.pop(0) + ', '
print(res[:-2])