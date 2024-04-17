name_list = input('Введите 4 имени через пробел: ').split()
rate_list = input('Введите 4 ставки через пробел: ').split()
rate_list = [int(i) for i in rate_list]
bonus_list = input('Введите 4 премии через пробел вида 10.25%: ').replace('%', '').split()
bonus_list = [float(i) for i in bonus_list]

list1 = []
for i in range(len(rate_list)):
    list1.append(rate_list[i]*bonus_list[i]/100)

#print(list1)
res={}
for i in range(len(name_list)):
    res[name_list[i]] = list1[i]
#print(res)
list1 = [rate_list[i]*bonus_list[i]/100 for i in range(len(rate_list))]
#gen1 = {name_list[i]: list1[i] for i in range(len(name_list))} 
gen1 = {name_list[i]: list(rate_list[i]*bonus_list[i]/100 for i in range(len(rate_list)))[i] for i in range(len(name_list))} 
print(list1, gen1)