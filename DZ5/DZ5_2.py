"""Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: имена str, ставка int, премия str 
с указанием процентов вида “10.25%”. В результате получаем словарь 
с именем в качестве ключа и суммой премии в качестве значения. Сумма рассчитывается как ставка умноженная на процент премии"""

name_list = input('Введите 4 имени через пробел: ').split()
rate_list = input('Введите 4 ставки через пробел: ').split()
rate_list = [int(i) for i in rate_list]
bonus_list = input('Введите 4 премии через пробел вида 10.25%: ').replace('%', '').split()
bonus_list = [float(i) for i in bonus_list]


dict_gen = {name_list[i]: list(rate_list[i]*bonus_list[i]/100 for i in range(len(rate_list)))[i] for i in range(len(name_list))} 

print(dict_gen)