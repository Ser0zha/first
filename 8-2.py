Library = {"Пушкин": ["Борис Годунов", "Евгений Онегин", "Моцарт и Сальери", "Пир во время чумы", "Каменный гость"],
           "Гоголь": ["Ревизор", "Женитьба", "Игроки", "Записки сумасшедшего", "Мертвые души"],
           "Лермонтов": ["Герой нашего времени", "Бородино", "Песня про царя Ивана Васильевича", "Мцыри", "Маскарад"]}
print("Дополнить или просмотреть? (add/view)")
f = True
message = input()
if message == "add":
    print("Выберите автора (Пушкин, Гоголь или Лермонтов):")
    out_author = input().strip()
    out_add = input().split()
    try:
        Library[out_author] += out_add
        print(*Library[out_author], sep=", ")
        exit()
    except KeyError:
        print("Введите корректный ответ")
        exit()
if message == 'view':
    print("Выберите автора (Пушкин, Гоголь или Лермонтов):")
    out_view = input()
    if Library.get(out_view):
        print(*Library[out_view], sep=", ")
    exit()
else:
    f = False
if not f:
    print("Введите корректный ответ")
    exit()
