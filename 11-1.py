string = input(">>>").split()
stack = list()
i = 0
if len(string) < 3:
    print("Введите строку более чет из одного символа")
    exit()
for i in range(len(string) // 2):
    stack.append(string[i])
i += (len(string) % 2) + 1
for i in range(i, len(string)):
    if stack.pop() != string[i]:
        print("Не полиндром")
        exit()
print("Полиндром")

# s = input()
# if s == s[::-1]:
#     print("yes")
# else:
#     print("no")
