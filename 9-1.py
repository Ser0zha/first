import os


def add_file(cnt1, vector1):
    for i in range(cnt1):
        vector1.pop()
    return vector1


path = './data/ex9.1-vector.txt'
if not os.path.exists(path):
    print("файла нет")
    exit()

with open(os.path.join('data', "ex9.1-vector.txt"), "r") as f:
    try:
        vector = [float(i) for i in f.readline().split(",")]
    except ValueError:
        print("Пустой файл или имеет некорректные значения")

try:
    cnt = int(input("Введите количество чисел для удаления: "))
    if (cnt < 0) or (cnt > len(vector)):
        print("Вы ввели не правильное значение!")
        exit()
except ValueError:
    print("Введите корректный ответ")
    exit()

diff = add_file(cnt, vector)
with open("./data/9.1output.txt", "w") as f:
    f.write(str(diff))
print(*diff, sep=" ")
