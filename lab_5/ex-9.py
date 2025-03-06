import re
with open(r"c:\Users\Asus\Desktop\python\PP_2\lab_5\row.txt", "r") as file:
    file1 = f.read()
file = "ThereAreSeveralGeeseInThePond"
pattern = "[A-Z][a-z]*"
match = re.findall(pattern, file)
a = ""
for i in match:
    a = a+(i)
    a += " "
print(a)
