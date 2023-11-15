string = input(">>>").split()
Stack = list()
i = 0
if len(string) < 3:
    print("Введите строку более чет из одного символа")
    exit()
for i in range(len(string) // 2):
    Stack.append(string[i])
# print(i)
i += (len(string) % 2) + 1
# print(">>>", i)
for i in range(i, len(string)):
    if Stack.pop() != string[i]:
        print("Не палиндром")
        exit()
print("Палиндром")

# s = input()
# if s == s[::-1]:
#     print("yes")
# else:
#     print("no")
