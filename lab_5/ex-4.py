import re

with open(r"c:\Users\Asus\Desktop\python\PP_2\lab_5\row.txt", "r", encoding="utf-8") as file:
    for line in file:  # Читаем файл построчно
        matches = re.findall(r"\b[A-Z][a-z]+\b", line)  # Ищем совпадения
        if matches:  # Если нашли хотя бы одно совпадение
            print(f"Found in line: {line.strip()} → {matches}")
