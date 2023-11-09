first = input("Введите первую строку:")
second = input("Введите вторую строку:")
set_a = set(first)
set_b = set(second)
diff = set_a.difference(set_b)
d = list(diff)
if diff == set():
    print("Все элементы встречаются во второй строке")
else:
    print("Элементы, которые встречаются в первой, но не во второй:")
    print(*d, sep=" ")
