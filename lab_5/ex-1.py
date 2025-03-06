import re

with open(r"c:\Users\Asus\Desktop\python\PP_2\lab_5\row.txt", "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        if re.fullmatch(r"ab*", line):
            print(f"Match found: {line}")
        else:
            print(f"No match: {line}")
