"""Напишите функцию, которая ищет json файлы в указанной директории и 
сохраняет их содержимое в виде одноимённых pickle файлов."""

import pickle
import json
import os

def json_to_pickle(dir='.'):
    for file in os.listdir(dir):
        file_name, file_exten = os.path.splitext(file)
        if file_exten == '.json':
            with open(os.path.join(dir, file), 'r', encoding='utf-8') as f:
                data = json.load(f)
            with open(os.path.join(dir, file_name + '.pickle'), 'wb') as f:
                pickle.dump(data, f)


if __name__ == '__main__':
    json_to_pickle()