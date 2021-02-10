def division(var1, var2):
    """
    Возвращает частное от деления var1 на var2, если эт возможно.

    :param var1: int/float
    :param var2: int/float
    :return: int/float
    """
    try:
        var = var1 / var2
        return var
    except ZeroDivisionError:
        return "Значенатель не должен быть 0"
    except ValueError:
        return "Введит епожалуйста только числа"


print(division((int(input("Введите 1-ое число: "))), (int(input("Введите 2-ое число: "))), ))
