def inputValue(arr, n, m):
    for i in range(n):
        for j in range(m):
            try:
                arr[i][j] = int(input())
            except ValueError:
                print("Введено некорректное значение")
                exit()
    return arr


def out(arr, n, m):
    for i in range(n):
        for j in range(m):
            print(arr[i][j], end=' ')
        print()
    return


print("Введите размеры матрицы порядка М * К и К * N")
M = 0
K = 0
N = 0
try:
    print("Введите M")
    M = int(input())
    print("Введите K")
    K = int(input())
    print("Введите N")
    N = int(input())
except ValueError:
    print("Введено некорректное значение")
    exit()

if (M or K or N) <= 0:
    print("Введено значения побольше")
    exit()

A = [[0 for i in range(K)] for j in range(M)]
B = [[0 for i in range(N)] for j in range(K)]
print("Введите значения матрицы А")
inputValue(A, M, K)
print("Введите значения матрицы B")
inputValue(B, K, N)
result = [[0 for i in range(M)] for j in range(N)]
for i in range(M):
    for j in range(N):
        result[i][j] = sum(A[i][o] * B[o][j] for o in range(K))

print("Матрица А")
print(out(A, M, K))
print("\nМатрица В")
print(out(B, K, N))
print("\nПроизведение")
print(out(result, M, N))
