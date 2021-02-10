def sum_2_max_el(var1, var2, var3):
    """
    Возваращет сумму двух максимальных элементов передоваемых в качестве параметров.

    :param var1: int/float
    :param var2: int/float
    :param var3: int/float
    :return: int/float
    """
    my_list = [var1, var2, var3]
    my_list.sort(reverse=True)
    return sum(my_list[:2])


print(sum_2_max_el((int(input("Введите 1-ое число: "))), (int(input("Введите 2-ое число: "))), (int(input("Введите 3-е число: ")))))
