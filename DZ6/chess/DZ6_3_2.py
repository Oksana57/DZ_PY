import itertools
from DZ6_3 import generate_queens


def queens ():
    for p in itertools.permutations (range (0, 8) ):
       yield [x for x in enumerate (p) ]

def wright_qween():
    list1 = []

    for q in queens():
        flag = False
        for a, b in ((a, b) for a in q for b in q if a[0] < b[0]):
            if abs (a[0] - b[0] ) == abs(a[1] - b[1]):
                flag = True
                break
        if not flag: list1.append(q)
    return list1


if __name__ == '__main__':
    #print(generate_queens())
    #print(wright_qween())
    wrightlist = wright_qween()
    #list2 = []
    list3 = []
    while len(list3) <= 3:
        list2 = []
        var1 = generate_queens()
        try :
            for i in range(len(var1)):
                for j in range(len(wrightlist[i])):
                    if str(var1[i]) == str(wrightlist[i][j]):
                        break
                        
                    else:
                        continue
                list2.append(var1[i])
            list3.append(list2)       
        except:
            break
        
    print(list3)

