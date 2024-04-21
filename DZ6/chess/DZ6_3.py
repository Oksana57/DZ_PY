"""Напишите функцию в шахматный модуль. 
Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше. 
Проверяйте различный случайные варианты и выведите 4 успешных расстановки."""

from random import randint as rnd

def generate_queens():
    queens = []
    while len(queens) < 8:
        x = rnd(0, 7)
        y = rnd(0, 7)
        if x not in queens and y not in queens:
            queens.append((x, y))
    return queens

if __name__ == '__main__':  
    print(generate_queens())