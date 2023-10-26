number_one = input(">>>")
number_two = input(">>>")
a = number_one.replace(number_two, "", number_one.count(number_two) - 1)
print(a)
