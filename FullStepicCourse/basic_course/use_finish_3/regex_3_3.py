import re
import sys
"""
Вам дана последовательность строк.
Выведите строки, содержащие "cat" в качестве подстроки хотя бы два раза.
"""
pattern = r'((cat).*){2,}'
for line in sys.stdin:
    line = line.rstrip()
    if re.search(pattern, line):
        print(line)

"""
Вам дана последовательность строк.
Выведите строки, содержащие "cat" в качестве слова.
"""
pattern = r'\bcat\b'
for line in sys.stdin:
    line = line.rstrip()
    if re.search(pattern, line):
        print(line)

"""
Вам дана последовательность строк.
Выведите строки, содержащие две буквы "z﻿", между которыми ровно три символа.
"""
pattern = r"(z.{3}z)"
for line in sys.stdin:
    line = line.rstrip()
    if re.search(pattern, line):
        print(line)

"""
Вам дана последовательность строк.
Выведите строки, содержащие обратный слеш "\﻿".
"""
pattern = r"\\.+"
for line in sys.stdin:
    line = line.rstrip()
    if re.search(pattern, line):
        print(line)

"""
Вам дана последовательность строк.
Выведите строки, содержащие слово, состоящее из двух одинаковых частей (тандемный повтор).
"""
pattern = r"\b(.+)\1\b"
for line in sys.stdin:
    line = line.rstrip()
    if re.search(pattern, line):
        print(line)

"""
Вам дана последовательность строк.
В каждой строке замените все вхождения подстроки "human" на подстроку "computer"﻿
и выведите полученные строки.
"""
pattern = r"human"
for line in sys.stdin:
    line = line.rstrip()
    new_line = re.sub(pattern, "computer", line)
    print(new_line)

"""
Вам дана последовательность строк.
В каждой строке замените первое вхождение слова, состоящего только из латинских
букв "a" (регистр не важен), на слово "argh".
"""
pattern = r"\b[Aa]+\b"
for line in sys.stdin:
    line = line.rstrip()
    new_line = re.sub(pattern, "argh", line, 1)
    print(new_line)

"""
Вам дана последовательность строк.
В каждой строке поменяйте местами две первых буквы в каждом слове, состоящем хотя бы из двух букв.
Буквой считается символ из группы \w.
"""
pattern = r"\b(\w)(\w)(\w*)\b"
for line in sys.stdin:
    line = line.rstrip()
    new_line = re.sub(pattern, r"\2\1\3", line)
    print(new_line)

"""
Вам дана последовательность строк.
В каждой строке замените все вхождения нескольких одинаковых букв на одну букву.
Буквой считается символ из группы \w.
"""