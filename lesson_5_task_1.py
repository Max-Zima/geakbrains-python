my_file = open('text_file.txt', 'w')
line = input('Введите данные: ')
while line:
    print(line + '\n', file=my_file)
    line = input('Введите данные: ')
