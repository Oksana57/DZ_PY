import os
import json
import csv
import pickle

def go_dir_and_file(directory):
    go_dir_res = {}
    for root, dirs, files in os.walk(directory):
        go_dir_res[f'Директория - {root}'] = {f'файл - {i} = {os.path.getsize(os.path.abspath(dirs + '/' + i))}' for i in dirs }
    with open('res_files.json', 'wb', encoding='utf-8') as f_js:
        json.dump(go_dir_res, f_js, indent=4, separators=(',', ':'))
