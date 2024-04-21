'''Напишите функцию в шахматный модуль. Используйте генератор случайных чисел 
для случайной расстановки ферзей в задаче выше. 
Проверяйте различный случайные варианты и выведите 4 успешных расстановки.'''

from DZ6_3 import generate_queens
from DZ6_2 import queens


if __name__ == '__main__':
       
    queens_list = []

    while len(queens_list) <= 3:
        
        var1 = generate_queens()
        if queens(var1) is False:
            continue    
        else:
            queens_list.append(var1) 

        print(queens_list)
     
   

