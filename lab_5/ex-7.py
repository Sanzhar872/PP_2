import re
with open(r"c:\Users\Asus\Desktop\python\PP_2\lab_5\row.txt", "r") as file:
    file1 = file.read()
file = "the_snake_case_inscription"
pattern = "_([a-z])"
match = re.findall(pattern, file)
for a in match:
    file = file.replace(f"_{a}", a.upper())
print(file)
