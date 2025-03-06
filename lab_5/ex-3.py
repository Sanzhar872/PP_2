import re

with open(r"c:\Users\Asus\Desktop\python\PP_2\lab_5\row.txt", "r", encoding="utf-8") as file:
    for line in file:
        matches = re.findall(r"\b[a-z]+_[a-z]+\b", line)
        if matches:
            print(f"Found in line: {line.strip()} → {matches}")
