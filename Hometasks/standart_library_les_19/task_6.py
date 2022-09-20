"""
Напишите скрипт для отображения различных форматов даты и времени.
  а) Текущая дата и время
  б) Текущий год
  в) Месяц года
  г) номер недели в году
  д) будний день недели
  е) День года
  г) день месяца
  з) День недели
"""


import datetime


if __name__ == '__main__':
    def date_time():
        return f'Дата и время: {datetime.datetime.now()}'


    def year():
        return f'Год: {datetime.datetime.now().year}'


    def month():
        _now = datetime.datetime.now()
        return f'Месяц: {datetime.datetime.now().month} ({_now.strftime("%B")})'


    def week_num():
        _now = datetime.datetime.now()
        return f'Номер недели в году: {_now.strftime("%W")}'


    def weekday():
        _now = datetime.datetime.now()
        return f'Рабочий день недели: {_now.strftime("%u")}'


    def day_of_year():
        _now = datetime.datetime.now()
        return f'Номер дня в году: {_now.strftime("%j")}'


    def day_of_month():
        _now = datetime.datetime.now()
        return f'Номер дня в месяце: {_now.strftime("%d")}'


    def day_of_week():
        _now = datetime.datetime.now()
        return f'День недели: {_now.strftime("%A")}'


    print(weekday())
