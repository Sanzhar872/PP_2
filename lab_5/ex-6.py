import re

with open(r"c:\Users\Asus\Desktop\python\PP_2\lab_5\row.txt", "r", encoding="utf-8") as file:
    file = file.read()
pattern = "[ ,.]+"
replacement = ":"
match = re.sub(pattern, replacement, file)
print(match)
