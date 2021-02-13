from functools import reduce

my_list = [int(el) for el in range(100, 1001, 2)]


def compos(var1, var2):
    """
    Возвращает произвдение 2 чисел, передоваемых в качаестве параметров.

    :param var1: int
    :param var2: int
    :return: int
    """
    return var1 * var2


print(reduce(compos, my_list))
