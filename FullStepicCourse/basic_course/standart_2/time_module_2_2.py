"""
В первой строке дано три числа, соответствующие некоторой дате date -- год, месяц и день.
Во второй строке дано одно число days -- число дней.
Вычислите и выведите год, месяц и день даты, которая наступит, когда с момента исходной даты
date пройдет число дней, равное days.
"""

import datetime
(y, m, d) = [int(n) for n in input().split()]
n = int(input())
date = datetime.date(y, m, d)
delta = datetime.timedelta(n)
date = date + delta
print(date.year, date.month, date.day)

