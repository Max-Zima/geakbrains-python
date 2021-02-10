def exponentiation_1(x, y):
    """
    Возвращает число x возведённое в степень y, использую степень.

    :param x: float
    :param y: int
    :return: float
    """
    return (x ** y)


def exponentiation_2(x, y):
    """
    Возвращает число x возведённое в степень y, используя цикл.

    :param x: float
    :param y: int
    :return: x в степени y
    """
    s = 1 / x
    for el in range(abs(y) - 1):
        s *= (1 / x)
    return s


print(exponentiation_1((float(input("Введите число: "))), (int(input("Введите в какую степень возвести число: ")))))
print(exponentiation_2((float(input("Введите число: "))), (int(input("Введите в какую степень возвести число: ")))))
