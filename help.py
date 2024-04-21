#import itertools
from DZ6.chess.DZ6_3 import generate_queens
from DZ6.chess.DZ6_2 import queens
# f = [(0, 3), (1, 7), (2, 0), (3, 2), (4, 5), (5, 1), (6, 6), (7, 4)]
# hit = False

# for i in range(8):
#     x1 = f[i][0]
#     y1 = f[i][1]
#     for ii in range(i+1, 8):
#         x2 = f[ii][0]
#         y2 = f[ii][1]
#         if x1 == x2 or y1 == y2 or abs(y2 - y1) == abs(x2 - x1):
#             hit = True
# if hit:
#     print('YES')
# else:
#     print('NO')

queens_list = []
#list3 = []
#while len(queens_list) <= 3:
    
f = generate_queens()
#try :
hit = False

for i in range(8):
    x1 = f[i][0]
    y1 = f[i][1]
    for ii in range(i+1, 8):
        x2 = f[ii][0]
        y2 = f[ii][1]
        if x1 == x2 or y1 == y2 or abs(y2 - y1) == abs(x2 - x1):
            hit = True
if hit:
    print(f)
    print('YES')
else:
    print(f)
    print('NO')
#     if queens(var1) is True:
#         continue    
#     else:
#         queens_list.append(var1) 

# print(queens_list)
