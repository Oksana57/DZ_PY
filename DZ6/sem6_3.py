"""Улучшаем задачу 2.
Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала.
Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
Для преобразования строковых аргументов командной строки в числовые параметры используйте генераторное выражение."""

from random import randint as rnd
from sys import argv


def guess_number(lower_limit=1, upper_limit=100, count_try=10):

    num = rnd(lower_limit, upper_limit)

    print(f'Угадай число от {lower_limit} до {upper_limit},которое я загадал, у тебя {count_try} попыток')
    while 1 <= count_try:

        a = int(input(f"Введи число {lower_limit} до {upper_limit}: "))
        if a == num:
            print(f"Ты угадал, это число {num}")
            break
        elif a < num:
            count_try-=1
            print(f"Нет мое число больше, у тебя осталось {count_try} попыток")
        elif a > num:
            count_try-=1
            print(f"Нет мое число меньше, у тебя осталось {count_try} попыток")

    else:
        print(f'Вы исчерпали количество попыток, мое число {num}')


if __name__ == '__main__':
    
    # n = len(argv)
    # match(n):
    #     case 1:
    #         lower_limit = 0
    #         upper_limit = 100
    #         count_try = 10
    #     case 2:
    #         upper_limit = 100
    #         count_try = 10
    #         lower_limit = int(argv[1])
    #     case 3:
    #         count_try = 10  
    #         lower_limit = int(argv[1])
    #         upper_limit = int(argv[2])
    #     case _:
    #         lower_limit = int(argv[1])
    #         upper_limit = int(argv[2])
    #         count_try = int(argv[3])

    # guess_number(lower_limit, upper_limit, count_try)
    guess_number(*map(int, argv[1:]))