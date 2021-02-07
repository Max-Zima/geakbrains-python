my_int = 123
my_float = 1.5
my_str = "String"
my_list = ['True', False, 156]
my_tuple = ('False', True, 651)
my_dict = {1: '1', 2: '2', 3: '3'}

big_list = [my_int, my_float, my_str, my_list, my_tuple, my_dict]
for el in big_list:
    print(f'{el} is {type(el)}')
