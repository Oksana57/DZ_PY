"""Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
Для простоты договоримся, что год может быть в диапазоне [1, 9999].
Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
Проверку года на високосность вынести в отдельную защищённую функцию."""

from sys import argv
from datetime import datetime as dt
from calendar import isleap


def check_date(date: str):
    try:
        t = dt.strptime(date, '%d.%m.%Y')
        _try_isleap(t.year)
        return True
    except:
        return False


def _try_isleap(year: int):
    print(f'високосный' if isleap(year) else 'невисокосный')


if __name__ == '__main__':
    #print(argv)
    print(check_date(*map(str, argv[1:])))
    #print(check_date(input('date: ')))
