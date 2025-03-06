import re
with open(r"c:\Users\Asus\Desktop\python\PP_2\lab_5\row.txt", "r") as file:
    file1 = file.read()
file = "There Are Several Geese In The Pond"
pattern = "[A-Z][a-z]*"
match = re.findall(pattern, file)
print(match)
