from collections import Counter
print("Введите массив:")
arr = [str(i) for i in input().split()]
first = Counter(arr).most_common()[0][0]
second = Counter(arr).most_common()[1][0]
if Counter(arr).most_common()[0][1] != Counter(arr).most_common()[1][1]:
    print("Мода массива:", first)
else:
    print("Моды не существует!")
