"""Напишите функцию, которая получает на вход директорию и рекурсивно 
обходит её и все вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle.
○ Для дочерних объектов указывайте родительскую директорию.
○ Для каждого объекта укажите файл это или директория.
○ Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней
 с учётом всех вложенных файлов и директорий."""

import os
import json
import csv
from sem8_5 import json_to_pickle

def go_dir_and_file(directory):
    """Напишите функцию, которая получает на вход директорию и рекурсивно 
обходит её и все вложенные директории."""
    # рекурсивное обхождение директорий и запись информации в словарь
    go_dir_res = {}
    for root, _, files in os.walk(directory):
        go_dir_res[f'Директория - {root}'] = \
            [f'файл - {i} = {os.path.getsize(os.path.abspath(root + "/" + i))} байт'
                                               for i in files]
    # запись словаря в json файл
    with open('res_files.json', 'w', encoding='utf-8') as f_js:
        json.dump(go_dir_res, f_js, indent=4, separators=(',', ':'))
    # запись словаря в csv файл
    db = []
    for k, v in go_dir_res.items():
        db.append([k,v])
    with open('res_file.csv', 'w', encoding='utf-8') as f_csv:  
        write_csv = csv.writer(f_csv, dialect='excel-tab', delimiter=',')
        write_csv.writerows(db)
    json_to_pickle('.') # из json в pickle
    

if __name__ == '__main__':
    go_dir_and_file('files')