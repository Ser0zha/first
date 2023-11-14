translate = {"Привет": "Hello", "Мир": "World", "Я": "I'm", "Машина": "Car", "Магия": "Magic", "Существо": "Creature"}
inp = input("Введите строку: ").split(" ")
inp = [i.capitalize() for i in inp]
out = [translate.get(i.capitalize()) if translate.get(i) else i for i in inp]
print("Перевод:\n", *out, sep='')
