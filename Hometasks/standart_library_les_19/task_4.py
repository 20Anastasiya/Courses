"""
Напишите программу Python для отображения календаря для в заданной локали. (модуль calendar)
"""


import calendar
import datetime
import locale


if __name__ == '__main__':
    locale.setlocale(locale.LC_TIME, "en_US.UTF-8")

    now = datetime.datetime.now()
    calendar.prmonth(now.year, now.month)
