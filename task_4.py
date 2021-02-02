n = abs(int(input("Введите целое положительное число: ")))
max = n % 10
n = n // 10
while (n > 0) and (max != 9):
    if (n % 10) > max:
        max = n % 10
    n = n // 10
print("Максимальное цифра в числе:", max)

