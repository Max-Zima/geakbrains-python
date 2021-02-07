def index_number(number):
    global my_list
    number_count = my_list.count(number)
    if number_count > 0:
        i = my_list.index(number)
        my_list.insert(i + number_count, number)
    elif number < my_list[len(my_list) - 1]:
        my_list.append(number)
    else:
        for el in my_list:
            if number > el:
                j = my_list.index(el)
                my_list.insert(j, number)
                break


my_list = [7, 5, 3, 3, 2]
digit = 10
while digit > 0:
    number = int(input("Введите число: "))
    index_number(number)
    print(my_list)
    check_str = (input("Вы хотите закончить изменение рейтинга?(Если нет - нажмите Enter) "))
    if len(check_str) > 0:
        digit = 0
