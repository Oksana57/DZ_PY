"""Напишите функцию, которая заполняет файл
(добавляет в конец) случайными парами чисел.
Первое число int, второе - float разделены вертикальной чертой.
Минимальное число - -1000, максимальное - +1000.
Количество строк и имя файла передаются как аргументы функции."""

import os
import random

def fill_file (count: int, file_name: str):
    """Заполняет файл числами."""

    min1 = -1000
    max1 = 1000
    with open(file_name, 'w', encoding='utf-8') as f:
        for i in range(count):
            f.write(f'{random.randint(min1, max1)} | {random.uniform(min1,max1)}')
            f.write('\n' if i < count-1 else '')


if __name__ == '__main__':
    fill_file(10, 'data.txt')