"""Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
Каждая группа включает файлы с несколькими расширениями.
В исходной папке должны остаться только те файлы, которые не подошли для сортировки."""

import os

DICTIONARY = {
    'txt': 'texts',
    'doc': 'texts',
    'jpg': 'picture',
    'png': 'picture'
}

def sort_files(directory):
    for f in os.listdir(directory):
        extention = f.rsplit('.')[-1]
        if extention not in DICTIONARY:
            continue
        new_directory = f'{directory}/{DICTIONARY[extention]}'
        try: 
            os.mkdir(new_directory)
        except:
               print() 
        os.rename(f'{directory}/{f}', f'{new_directory}/{f}')    


if __name__ == "__main__":
     sort_files('files')    
