"""Напишите функцию, которая открывает на чтение созданные
в прошлых задачах файлы с числами и именами.
Перемножьте пары чисел. В новый файл сохраните
имя и произведение:
если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
В результирующем файле должно быть столько же строк, сколько в более длинном файле.
При достижении конца более короткого файла,
возвращайтесь в его начало."""


def read_begin(fd):
    text = fd.readline()
    if text == '':
        fd.seek(0)
        text = fd.readline()
    return text[:-1]

def process_file(file1, file2, file_res):
    with open(file1, 'r', encoding='utf-8') as f1:
        with open(file2, 'r', encoding='utf-8') as f2:
            with open(file_res, 'w', encoding='utf-8') as fr:
                lengh1 = len(f1.readlines())
                lengh2 = len(f2.readlines())
                lengh = max(lengh2, lengh1)
                for _ in range(lengh):
                    line_f1 = read_begin(f1)
                    line_f2 = read_begin(f2)
                    a, b = line_f1.split('|')
                    res = int(a) * float(b)
                    if res < 0:
                        res *=-1
                        line_f2 = line_f2.lower()
                    else:
                        res = round(res) 
                        line_f2 = line_f2.upper()   
                    fr.write(f'{line_f2} {res}') 
                    fr.write('\n' if _ < lengh else '')


if __name__ == '__main__':
    process_file('data.txt', 'name.txt', 'res.txt')           