first = input("Введите первую строку:")
second = input("Введите вторую строку:")
if first.isdigit() and second.isdigit():
    print("Введено некорректное значение")
else:
    set_a = set(first)
    set_b = set(second)
    diff = set_a.intersection(set_b)
    d = list(diff)
    d.remove(" ")
    print("Ответ:")
    print(*d, sep=" ")
