str_inv = input().strip()
stack = list()
for i in range(len(str_inv)):
    stack.append(str_inv[i])
for i in range(len(str_inv)):
    print(stack.pop(), end="")
