import json
profit = {}
pr = {}
prof = 0
prof_aver = 0
i = 0
with open('file_7.txt', 'r') as file:
    for line in file:
        name, firm, earning, damage = line.split()
        profit[name] = int(earning) - int(damage)
        if profit.setdefault(name) >= 0:
            prof += profit.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
        print(f'Прибыль средняя - {prof_aver: .2f}')
    else:
        print('Прибыль средняя - отсутсвует. Все работают в убыток')
    pr = {'Средняя прибыль': round(prof_aver)}
    profit.update(pr)
    print(f'Прибыль каждой компании:\n{profit}')

with open('file_7.json', 'w') as js_file:
    json.dump(profit, js_file)
    js_str = json.dumps(profit)
    print(f'Создан файл с расширением json со следующим содержимым:\n{js_str}')