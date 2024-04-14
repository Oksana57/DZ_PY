""" Дан список повторяющихся элементов. 
Вернуть список с дублирующимися элементами. 
В результирующем списке не должно быть дубликатов"""

from collections import Counter

lst_el = [1, 34, 2, 1, 35, 1, 2, 34, 3, 5]
dct_dubl = Counter(lst_el)
#print(dct_dubl)

lst_dubl = []
for k, v in dct_dubl.items():
    if v > 1:
        lst_dubl.append(k)
    else:
        continue
print(list(set(lst_dubl)))