"""
Вашей программе на вход подаются три строки s, a, b, состоящие из строчных латинских букв.
За одну операцию вы можете заменить все вхождения строки a в строку s на строку b.
Выведите одно число – минимальное число операций, после применения которых в строке s не
останется вхождений строки a, или Impossible, если операций потребуется более 1000.
"""
s = input()
a = input()
b = input()
s1 = s
x = 0
while a in s1:
    s1 = s1.replace(a, b)
    if s1 == s or x>1000:
        x = 'Impossible'
        break
    else:
        x += 1
print(x)

"""
Вашей программе на вход подаются две строки s и t, состоящие из строчных латинских букв.
Выведите одно число – количество вхождений строки t в строку s.
"""

s = str(input())
t = str(input())

def t_count(s, t):
    return 0 if len(s) < len(t) else s.startswith(t) + t_count(s[1:], t)

print(t_count(s, t))
