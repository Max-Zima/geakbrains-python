def my_sum():
    """
    Возвращет сумму вводимых чисел.

    :return: int
    """
    sum_res = 0
    ex = True
    while ex:
        number = input('Вводите сила или Q для выхода - ').split()
        res = 0
        for el in range(len(number)):
            if number[el] == 'q' or number[el] == 'Q':
                ex = False
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
    return sum_res


print(my_sum())
