#Write a program that takes an input list of numbers in one
# line and displays in a single line the values that repeat it more than once.
#Test1
from collections import Counter
a = [int(i)for i in input().split()]
c = Counter(a)
w=[]
print(c)
array_d = {}.fromkeys(a,0)
for i in a:
    array_d[i]+=1
result = {i:a.count(i) for i in a}
w=array_d.values()
print(w)
for key, value in c.items():
    if value==1:
        print('')
    else:
        print(value, end=' ')

#Test2
from collections import Counter
a = [int(i) for i in input().split()]
c = Counter(a)
for key, value in c.items():
    if value==1:
        print('')
    else:
        print(key, end=' ')