season_list = ['winter', 'spring', 'summer', 'autumn']
seasons_dict = {1: 'winter', 2: 'spring', 3: 'summer', 4: 'autumn'}
month = int(input('Введите номер месяца по счёту: '))
k = month // 3  # k переменная созданная для определения сезона по порядку
if k == 4:
    k -= 4
print(season_list[k])
print(seasons_dict.get(k + 1))
