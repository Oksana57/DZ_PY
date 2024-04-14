"""Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. 
Функцию hex используйте для проверки своего результата."""

BASE = 16

num = int(input('Введите целое цисло: '))
print(hex(num))
dict1 ={0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
n = None
s = None
res = ""

while num > BASE:
    n = num//BASE
    s = num - (n * 16)
    for k, v in dict1.items():
        if k == s:

            res += str(v)
   # res += str(num - n*16)
    num = n
res += str(num)

print(res[::-1])