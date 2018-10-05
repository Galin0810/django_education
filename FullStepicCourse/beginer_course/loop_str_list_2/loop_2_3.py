"""
Напишите программу, на вход которой даются четыре числа a, b, c и d, каждое в своей строке.
Программа должна вывести фрагмент таблицы умножения для всех чисел отрезка [a;b] на все числа
отрезка [c;d].
"""

a, b, c, d = [int(input()) for i in range(4)]
table = [[i * j for j in range(c, d + 1)] for i in range(a, b + 1)]
sep = "\t"
for i in range(c, d + 1):
    print(i, end=sep)
print()
for i in range(a, b + 1):
    print(i, end=sep)
    for j in table[i - a]:
        print(j, end=sep)
    print()

"""
Напишите программу, которая считывает с клавиатуры два числа a и b, считает и выводит на консоль
среднее арифметическое всех чисел из отрезка [a;b], которые делятся на 3.
"""

a = int(input())
b = int(input())
t = 0
ser = 0.0
count = 0
for i in range(a,b+1):
    if i % 3 == 0:
        t += i
        count += 1
        ser = float(t/count)
print(ser)