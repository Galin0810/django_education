#Output *********/////
n = int (input())
for i in range(n):
    for j in range(n):
        print("*", end='')
    print()
from itertools import product
for i,j in product(range(1,10),range(1,10)):
    print (i,j)
a = int(input())
b = int(input())
c = int(input())
d = int(input())
for i in range(a,b+1):
    for j in range(c, d+1):
        print(i*j, end='\t')
    print()
