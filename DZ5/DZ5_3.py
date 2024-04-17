"""Создайте функцию генератор чисел Фибоначчи"""

def fibonachi(num):
    a = 0
    b = 1
    list1 = []
    list1.append(a)
    for _ in range(num):
        a, b = b, a + b
        list1.append(a)
    return list1

print(fibonachi(11))   