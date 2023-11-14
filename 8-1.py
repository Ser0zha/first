dictionary = {"Ivanov": 20, "Sidorov": 68, "Petrov": 26, "Smirnov": 68}
k = ''
dictionary["Kolchin"] = 80
dictionary["Krivov"] = 70
m = max(dictionary.values())
mm = min(dictionary.values())
avg = sum(dictionary.values()) / len(dictionary)
maxi = [i for i in dictionary if dictionary.get(i) == m]
mini = [i for i in dictionary if dictionary.get(i) == mm]
for i in dictionary:
    if dictionary[i] > avg:
        k += i + " "
print(f"Студенты баллы которых выше среднего: \n{k}\n")
print(f"Минимальный балл: {mm} ", *mini, sep="")
print(f"Максимальный балл: {m} ", *maxi, sep="")
print(f"Средний балл: {avg: .1f}")
