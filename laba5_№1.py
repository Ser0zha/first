import re

flag = 1
while flag == 1:
    ent_s = input(">>>")
    if not ent_s:
        flag = 0
    else:
        check = r"^[^\<\>\/\\|\?\*]+\.(txt|doc|docx|odt|rtf)$"
        match = re.match(check, ent_s)
        if match:
            print("Этот файл может быть текстовым")
        else:
            print("Этот файл не может быть текстовым")
