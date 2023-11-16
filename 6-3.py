from collections import Counter
arr = input("Введите массив:").split()
first = Counter(arr).most_common()[0][0]
if Counter(arr).most_common()[0][1] != Counter(arr).most_common()[1][1]:
    print("Мода массива:", first)
else:
    print("Моды не существует!")
