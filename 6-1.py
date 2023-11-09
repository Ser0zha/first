def dev(arr):
    i = 0
    while i < size:
        try:
            arr.append(int(input()))
            i += 1
        except ValueError:
            print("Введено некорректное значение")
            exit()
    return arr


size = 0
A = []
B = []
print("Введите размеры векторов")
try:
    size = int(input())
except ValueError:
    print("Введено некорректное значение")
    exit()

if size <= 0:
    print("Введено некорректное значение")
    exit()
print("Вектор а")
A = dev(A)
print("Вектор б")
B = dev(B)
res = sum(map(lambda a, b: a * b, A, B))
print(res)
