# Если можно сразу подсчитывать
try:
    with open('file_5.txt', 'w+') as file_5:
        line = input('Введите цифры через пробел \n')
        file_5.writelines(line)
        print(sum(map(int, line.split())))

except IOError:
    print('Ошибка в файле')

except ValueError:
    print('Неправильно набран номер. Ошибка ввода-вывода')


# Если подсчитывать после создания файла
with open('file_5.txt') as file_5:
    line = file_5.readline()
    print(sum(map(int, line.split())))