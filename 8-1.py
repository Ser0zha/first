Dictionary = {"Ivanov": 20, "Sidorov": 68, "Petrov": 26, "Smirnov": 68}
k = ''
Dictionary["Kolchin"] = 80
Dictionary["Krivov"] = 70
m = max(Dictionary.values())
mm = min(Dictionary.values())
avg = sum(Dictionary.values()) / len(Dictionary)
maxi = [i for i in Dictionary if Dictionary.get(i) == m]
mini = [i for i in Dictionary if Dictionary.get(i) == mm]
for i in Dictionary:
    if Dictionary[i] > avg:
        k += i + " "
print(f"Студенты баллы которых выше среднего: \n{k}\n")
print(f"Минимальный балл: {mm} ", *mini, sep="")
print(f"Максимальный балл: {m} ", *maxi, sep="")
print(f"Средний балл: {avg: .1f}")
