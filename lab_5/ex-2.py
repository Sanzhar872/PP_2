import re

with open(r"c:\Users\Asus\Desktop\python\PP_2\lab_5\row.txt", "r", encoding="utf-8") as file:
    for line in file:
        if re.fullmatch(r"ab{2,3}", line.strip()):
            print(f"Match found: {line.strip()}")
