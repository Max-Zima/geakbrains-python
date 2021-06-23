from itertools import count, cycle


def qwerty(start_digit, finish_digit):
    """
    Возваращет целые числа, начиная с start_digit и заканчивая finish_digit.

    :param start_digit: int
    :param finish_digit: int
    :return: int
    """
    for el in count(start_digit):
        if el > finish_digit:
            break
        print(el, end=' ')


def qwerty1(my_list, max_iteration):
    """
    Повторяет элементы списка my_list, определенного заранее.Кол-во вхождений: max_iteration.

    :param my_list: list
    :param max_iteration: int
    :return: None
    """
    iter = cycle(my_list)
    i = 0
    while i < max_iteration:
        print(next(iter), end=' ')
        i += 1


qwerty(int(input("Введите начальное число: ")), int(input("Введите конечно число: ")))
print(end='\n')
qwerty1([el for el in input('Введите массив: ').split(' ')], int(input("Введите число повторений: ")))
