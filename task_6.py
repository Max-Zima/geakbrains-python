result_km = int(input("Введите результаты пробежки первого дня в км: "))
b = int(input("Введите общий желаемый результат в км: "))
result_days = 1
while result_km < b:
    result_km = result_km + (result_km * 0.1)
    result_days += 1
print(f"Вы достигнете требуемых показателей на {result_days} день")
print(f"На {result_days}-й день спортсмен достиг результата — не менее {b} км.")