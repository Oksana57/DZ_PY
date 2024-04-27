""" Напишите функцию группового переименования файлов. Она должна:
a. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
b. принимать параметр количество цифр в порядковом номере.
c. принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
d. принимать параметр расширение конечного файла.
e. принимать диапазон сохраняемого оригинального имени. 
Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. 
К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение."""

import os

def rename_files(new_name: str, 
                count_number: int, 
                old_extention: str, 
                new_extention: str, 
                range_letter: list,
                directory: str):
    if count_number == 1:
         n_min = 0
         n_max = 10
    elif count_number == 2:
        n_min = 10
        n_max = 100
    else:
        n_min = 100
        n_max = 1000
    for i in range(n_min, n_max):
        for f in os.listdir(directory):
            f0 = f.rsplit('.')[-1]
            if f0 == old_extention:
                f1 = f.split('.')[0:]
                #f2 = f1[3: 6]
                f2 = f1[range_letter[0]: range_letter[1]]                
                f3 = f'{f2}{new_name}{i}'
                l = list[f3, new_extention]
                new_f = str(f3)+'.'+str(new_extention)
                os.rename(f'{directory}/{f}', f'{directory}/{new_f}')
            else: 
                continue    


if __name__ == "__main__":
    rename_files('fils', 2, 'rnd', 'txt', [5, 9], 'files')   