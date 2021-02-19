class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": int(wage), "bonus": int(bonus)}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def total_income(self):
        return self._income["wage"] + self._income["bonus"]


p = Position(input("Введите имя работника: "), input("Введите фамилию работника: "),
             input("Введите долность работника: "), int(input("Введите зарплату работника: ")),
             int(input("Введите премию работника: ")))

print(p.get_full_name(), p.total_income())
