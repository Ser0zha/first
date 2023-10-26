import re

print(">>>")
car_number = input()

flag = re.match(r"[a-zA-Z]{2}\d{3}[a-zA-Z]", car_number)

if flag:
    print(car_number, "можно считать номером автомобиля")
else:
    print(car_number, "нельзя считать номером автомобиля")
