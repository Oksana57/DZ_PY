""" Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. 
Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны 
с суммой двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника 
с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним, равнобедренным 
или равносторонним."""

a, b, c = [int(s) for s in input("Введите значения трех сторон теругольника через пробел: ").split()]
if a + b < c or b + c < a or a + c < b:
    print("Такого треугольника не существует")
else:
    print("Да это треугольник", end=" ")
    if a == b or b == c or a == c:
        print("и это равнобедренный треугольник")
    elif a == b == c:
        print("и это равносторонний треугольник")
    else:
        quit
