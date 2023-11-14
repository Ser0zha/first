Translate = {"Привет": "Hello", "Мир": "World", "Я": "I'm", "Машина": "Car", "Магия": "Magic", "Существо": "Creature"}
Inp = input("Введите строку: ").split(" ")
Inp = [i.capitalize() for i in Inp]
Out = [translate.get(i.capitalize()) if translate.get(i) else i for i in Inp]
print("Перевод:\n", *Out, sep='')
