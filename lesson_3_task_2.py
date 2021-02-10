def oytput_info(name, surname, year, city, email, phone):
    """
    Выводит на экран передоваемые параметры.

    :param name: str
    :param surname: str
    :param year: int
    :param city: str
    :param email: str
    :param phone: str/int
    :return: None
    """
    print(name, surname, year, city, email, phone)
    return


oytput_info((input("Введите ваше имя: ")), (input("Введите вашу фамилию: ")),
            (int(input("Введите год вашего рождения: "))), (input("Введите город проживания: ")),
            (input("Введите ваш email: ")), (input("Введите ваш номер телефона: ")))
