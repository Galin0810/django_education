"""
Напишите программу, на вход которой подается одна строка с целыми числами. Программа должна вывести
сумму этих чисел. Используйте метод split строки. ﻿﻿
"""
from collections import Counter

a = [int(i) for i in input().split()]
b = sum(a[0:len(a)])
print(b)

"""
Напишите программу, на вход которой подаётся список чисел одной строкой. Программа должна для каждого
элемента этого списка вывести сумму двух его соседей. Для элементов списка, являющихся крайними,
одним из соседей считается элемент, находящий на противоположном конце этого списка. Например, если
на вход подаётся список "1 3 5 6 10", то на выход ожидается список "13 6 9 15 7" (без кавычек).
Если на вход пришло только одно число, надо вывести его же. Вывод должен содержать одну строку с
числами нового списка, разделёнными пробелом.
"""

q = [int(i) for i in input().split()]
if len(q) == 1:
    print(q[0])
else:
    w = []
    sum = []
    w.insert(0,q[-1])
    w+=q
    w.append(w[1])
    for j in range(1,len(w)-1):
        sum = w[j-1] + w[j+1]
        print(sum, end=' ')

"""
Напишите программу, которая принимает на вход список чисел в одной строке и выводит на экран в одну
cтроку значения, которые повторяются в нём более одного раза. Для решения задачи может пригодиться
метод sort списка.
"""

a = [int(i) for i in input().split()]
c = Counter(a)
for key, value in c.items():
    if value == 1:
        print('')
    else:
        print(key, end=' ')

"""

"""
