"""Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
 Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. 
 Достаточно вернуть один допустимый вариант.*Верните все возможные варианты комплектации рюкзака.

"""

dct_bag= {
    'спальник' : 0.5 ,
    'примус': 1.5,
    'крупа': 1.0,
    'консервы': 0.8 ,
    'палатка': 5.0,
    'кастрюля': 0.5,
    'сковорода': 0.8,
    'фонарь': 0.2,
    }
    
weight = 6.0
count1 = 0

lst_bag = []

for k, v in dct_bag.items():
    if count1 + v < weight:
        lst_bag.append(k)
        count1 += v
    else:
        continue
print(lst_bag)