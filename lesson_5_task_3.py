salary_up_to = []
i = 0
sum_salary = 0
with open('text_file.txt') as text_file:
    line = text_file.readline()
    while line:
        employee = line.split()
        surname = employee[0]
        salary = int(employee[1])
        if salary < 20000:
            salary_up_to.append(surname)
        sum_salary += salary
        i += 1
        line = text_file.readline()
print(f'Список сотрудников получающих до 20000 {salary_up_to}')
print(f'Средняя заработная плата {sum_salary / i}')
