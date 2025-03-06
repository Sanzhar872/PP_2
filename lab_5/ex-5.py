import re
with open(r"c:\Users\Asus\Desktop\python\PP_2\lab_5\row.txt", "r") as file:
    file = file.read()
pattern = r"a+\w*b\b"
match = re.findall(pattern, file)
print(match)
