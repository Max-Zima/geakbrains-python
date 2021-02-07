# my_str = input('Введите строчку: ')
# my_list = list(my_str.split())
# print(' '.join(my_list)) #Можно ли как-то в таком выводе ограничить количество выводимых элементов?

my_str = input('Введите строчку: ')
my_list = list(my_str.split())
for el in my_list:
    print(el[0:10], end=' ')
    
