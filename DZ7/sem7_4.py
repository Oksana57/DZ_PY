"""Создайте функцию, которая создаёт файлы с указанным расширением.
Функция принимает следующие параметры:
расширение
минимальная длина случайно сгенерированного имени, по умолчанию 6
максимальная длина случайно сгенерированного имени, по умолчанию 30
минимальное число случайных байт, записанных в файл, по умолчанию 256
максимальное число случайных байт, записанных в файл, по умолчанию 4096
количество файлов, по умолчанию 42
Имя файла и его размер должны быть в рамках переданного диапазона."""
import random
import os

MIN_COD = ord('a')
MAX_COD = ord('z')

def generator_text(length):
    """Генерируем имя."""
    name_file = []
    for i in range(length):
        name_file.append(chr(random.randint(MIN_COD, MAX_COD)))
    return ''.join(name_file)

def generate_files(extention,
                   directory,
                  min_length = 6, max_length = 30,
                  min_size = 256, max_size = 4096,
                  count_file = 12):
        """Генерирует файлы с параметрами"""
        try:
        #if not os.path.exists(directory) or os.path.isdir(directory):
                os.mkdir(directory)
        except:
               print()      
        
               
        for _ in range(count_file):
                name_length = random.randint(min_length, max_length)
                filename = generator_text(name_length)
                text_length = random.randint(min_size, max_size)
                text = generator_text(text_length)
                while True:
                        try:  
                                with open(f'{directory}/{filename}.{extention}', 'w', encoding='utf-8') as f:
                                        f.write(text)
                        except:
                               filename = generator_text(name_length)
                        else:
                               break


if __name__ == "__main__":
    generate_files('rnd', 'files')


