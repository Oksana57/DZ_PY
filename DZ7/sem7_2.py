"""Напишите функцию, которая генерирует псевдоимена.
Имя должно начинаться с заглавной буквы,
состоять из 4-7 букв, среди которых
обязательно должны быть гласные.
Полученные имена сохраните в файл."""

import random

MIN_LEN = 4
MAX_LEN = 7
MIN_COD = ord('a')
MAX_COD = ord('z')
VOWELS ={'a', 'e', 'y', 'u', 'i', 'o'}

def generator_name(file_name: str, count1: int):
    """Генерирует псевдоименаю"""
    with open(file_name, 'w', encoding='utf-8') as f:
        for _ in range(count1):
            len_name = random.randint(MIN_LEN, MAX_LEN)
            name_list = []
            for i in range(len_name):
                name_list.append(chr(random.randint(MIN_COD, MAX_COD)))
            has_vowels = False
            for letter in name_list:
                if letter in VOWELS:
                    has_vowels = True
                    break
            if not has_vowels:
                ind = random.randint(0, len(name_list)-1)
                letter_change = random.choice(list(VOWELS))
                name_list[ind] = letter_change
            print(f'{"".join(name_list).capitalize()}', file=f, end='')
            f.write('\n' if _ < count1-1 else '')
        
   

if __name__ == '__main__':
    generator_name('name.txt', 15)