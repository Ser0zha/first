import random

rnd = random.randint(4, 30)
flag = 0


def bot(x1):
    if x1 / 3 > 1:
        x1 -= 3
        return x1
    elif x1 / 2 > 1:
        x1 -= 2
        return x1
    elif x1 / 1 > 0:
        x1 -= 1
        return x1
    return 0


try:
    print(f"Имеется кучка из {rnd} камней")
    while flag == 0:
        number = int(input(">>>"))
        flag = 1
        if number == 1 or number == 2 or number == 3:
            rnd -= number
            print(f"\t Осталось {rnd} камней")
            if rnd == 1:
                print("\nТуда этого трансформера")
                break
            elif rnd < 1:
                print("Ты поступил глупо")
                break
            decepticon = bot(rnd)
            print(f"Робот сделал свой ход, осталось {decepticon} камней")
            rnd = decepticon
            if rnd == 1:
                print("\nТрансформер победил тебя")
                break
            flag = 0
            if rnd <= 1:
                flag = 1
                exit()
        else:
            print("Вы ввели число не по правилам :(")
            exit()
except ValueError:
    print("Введен неверный формат!")
    exit()
except KeyboardInterrupt:
    print("\nИгра завершина")
    exit()
# "!"
