my_list = [int(el) for el in input('Введите массив: ').split(' ')]
new_list = [el for i, el in enumerate(my_list) if el > my_list[my_list.index(el) - 1] and (i > 0)]
print(new_list)
