def word_count(string):
    """
    Возвращет кол-во слов в строке string.

    :param string: str
    :return: int
    """
    return len(string.split())


with open('text_file.txt') as text_file:
    line = text_file.readline()
    i = 1
    while line:
        k = word_count(line)
        print(f'В {i}-ой строке {k} слов')
        line = text_file.readline()
        i += 1
