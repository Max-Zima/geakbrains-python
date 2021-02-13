def fact(n):
    """
    Возвращает фактериал числа.

    :param n: int
    :return: int
    """
    tmp = 1
    for i in range(1, n + 1):
        tmp *= i
        yield tmp


n = int(input("Укажите факториал какого числа вы хотели бы узнать: \n"))
for el in fact(n):
    print(el)
