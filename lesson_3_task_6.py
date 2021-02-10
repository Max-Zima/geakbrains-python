def int_func(word):
    """
     Возвращает слово с первой заглавной буквой.

    :param word: str
     :return: str
     """
    return word.title()


def output_new_int_func(string):
    """
    Возвращает строку, в кторой каждое слово будет начинаться с заглвной буквы.

    :param string: str
    :return: str
    """
    separate_word = string.split()
    for el in separate_word:
        str_el = str(el)
        print(int_func(str_el), end=' ')
    return


output_new_int_func(input("Введите строку: "))
