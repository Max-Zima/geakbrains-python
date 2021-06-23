proceeds = int(input("Введите выручку фирмы:"))
costs = int(input("Введите издержки фирмы:"))
if proceeds > costs:
    print(f"Фирма работает с прибылью. Рентабельность выручки составила: {proceeds / costs}")
    workers = int(input("Введите количество сотрудников фирмы: "))
    print(f"Прибыль в расчете на одного сторудника сотавила {(proceeds - costs) / workers}")
elif proceeds == costs:
    print("Фирма работает в ноль.")
else:
    print("Фирма работает в убыток.")
