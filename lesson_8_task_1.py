class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        day, month, year = map(int, day_month_year.split('/'))
        date = (cls, day, month, year)
        return date

    @staticmethod
    def is_date_valid(day, month, year):
        if 0 < day <= 31 and 1 <= month <= 12 and 0 < year <= 2021:
            return day, month, year
        else:
            return 'Ошибка ввода данных'


today = Data('11/1/2001')
print(today)
print(Data.extract('11/11/2011'))
print(today.extract('11/11/2020'))
print(Data.is_date_valid(11, 11, 2022))
print(today.is_date_valid(11, 13, 2011))
print(Data.is_date_valid(1, 11, 2000))

