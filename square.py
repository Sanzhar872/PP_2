# Пользователь вводит размер квадрата
size = int(input("Введите размер квадрата: "))

for i in range(size):  # Проходим по строкам
    for j in range(size):  # Проходим по символам в строке
        # Рисуем символ только для границ квадрата
        if i == 0 or i == size - 1 or j == 0 or j == size - 1:
            print("* ", end="")
        else:
            print("  ", end="")
    print()  # Переход на новую строку после окончания текущей строки