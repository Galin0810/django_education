"""
В данной задаче мы просим вас реализовать класс multifilter,
который будет выполнять ту же функцию, что и стандартный класс filter, но будет использовать не одну
функцию, а несколько.
"""

def mul2(x):
    return x % 2 == 0

def mul3(x):
    return x % 3 == 0

def mul5(x):
    return x % 5 == 0

a = [i for i in range(31)]  # [0, 1, 2, ... , 30]

class multifilter:
    def judge_half(pos, neg):
        # допускає елемент, якщо допускає його хоча б половина функцій (pos >= neg)
        return pos >= neg

    def judge_any(pos, neg):
        # допускає елемент, якщо допускає його хоча б одна функція (pos >= 1)
        return pos >= 1

    def judge_all(pos, neg):
        # допускає елемент, якщо його допускають всі функції(neg == 0)
        return neg == 0

    def __init__(self, iterable, *funcs, judge=judge_any):
        # iterable - вихідна послідовність
        # funcs - допущені функції
        # judge - вирішальні функції
        self.iterable = iterable
        self.funcs = funcs
        self.judge = judge

    def __iter__(self):
        # повертає ітератор результативної функції
        for el in self.iterable:
            pos = 0
            neg = 0
            for func in self.funcs:
                if func(el):
                    pos += 1
                else:
                    neg += 1
            if self.judge(pos, neg):
                yield el

"""
Реализуйте функцию-генератор primes, которая будет генерировать простые числа в порядке возрастания,
начиная с числа 2.
"""

import itertools
import math

def is_prime(x):
    if x % 2:
        for x1 in range(3, int(math.sqrt(x)) + 1, 2):
            if x % x1 == 0:
                return False
        return True
    else:
        return False

def primes(x=2):
    while(True):
        if x == 2:
            yield x
        if is_prime(x):
            yield x
        x = x + 1

print(list(itertools.takewhile(lambda x: x <= 31, primes())))
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

