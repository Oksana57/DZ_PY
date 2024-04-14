"""Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
Программа должна возвращать сумму и произведение* дробей. 
Для проверки своего кода используйте модуль fractions"""

import fractions
import math

a, b = [int(s) for s in input('введите простую дробь видв a/b: ').split('/')]
c, d = [int(s) for s in input('введите вторую простую дробь видв a/b: ').split('/')]

f1 = fractions.Fraction(a, b)
f2 = fractions.Fraction(c, d)

print(f1 + f2, f1 * f2)


def sum_fract (a,b,c,d):
    if b == d:
        a1 = a + c
        l = math.gcd(a1, b)
        if True:
            a2 = int(a1/l)
            b2 = int(b/l)
            if a2 == b2:
                return 1
            else:
                return str(a2) + '/' + str(b2)
        else:
            return str(a1) + '/' + str(b)
    else:
        b1 = int(b * d)
        a1 = int(a*(b1/b)+c*(b1/d))
        s = math.gcd(a1, b1)
        a2 = int(a1 / s)
        b2 = int(b1 / s)
        return str(a2) + '/' + str(b2)


def mult_fract (a,b,c,d):
    a1 = a*c
    b1 = b*d


    l = math.gcd(a1, b1)
    if True:
        a2 = int(a1 /l)
        b2 = int(b1 /l)
        return str(a2) + '/' + str(b2)
    else:
        return str(a1) + '/' + str(b1)
    
print(sum_fract(a,b,c,d), mult_fract(a,b,c,d))    