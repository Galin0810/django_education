"""
Вашей программе на вход подаются две строки, содержащие url двух документов A и B.
Выведите Yes, если из A в B можно перейти за два перехода, иначе выведите No.
"""
import requests
import re

result = False

link_first = input()
res_first = requests.get(link_first)
if res_first.status_code == 200:
    link_second = input()
    for link in re.findall(r"<a href=\"(.*)\"", res_first.text):
        res = requests.get(link)
        if res.status_code == 200:
            for url in re.findall(r"<a href=\"(.*)\"", res.text):
                if link_second == url:
                    result = True
                    break
            if result:
                break
else:
    result = False

if result:
    print("Yes")
else:
    print("No")
