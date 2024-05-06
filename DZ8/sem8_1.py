"""Вспоминаем задачу 3 из прошлого семинара. Мы сформировали текстовый файл с псевдо именами и произведением чисел.
Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON.
Имена пишите с большой буквы.
Каждую пару сохраняйте с новой строки."""

import json

def file_pack(file_name = 'res.txt'):
    with open(file_name, 'r', encoding= 'utf-8') as f, \
        open('res.json', 'w', encoding='utf-8') as f2:
        json_list = []
        for line in f:

            json_list.append(line.capitalize())
        json.dump(json_list, f2, indent=4)    


if __name__ == '__main__':
    file_pack()