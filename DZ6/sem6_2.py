"""Создайте модуль с функцией внутри.
Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток.
Функция выводит подсказки “больше” и “меньше”.
Если число угадано, возвращается истина, а если попытки исчерпаны - ложь."""

from random import randint as rnd

def guess_number(lower_limit, upper_limit, count_try):

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
    a = int(input('Введите нижнюю границу'))
    b = int(input('Введите верхнюю границу'))
    c = int(input('Введите количество попыток'))
    guess_number(a, b, c)