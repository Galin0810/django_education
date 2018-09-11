# програма вычисляет процентное содержание символов G(гуанин) и С(цитозин) в введенной строке
# программа не должна зависеть от регистра вводимых символов)
s = "acggtgttat"
p = 0.0
c = 0
l = 0
c = s.upper().count("g".upper())
c += s.upper().count("c".upper())
for n in s:
    l += 1
print(c)
print(l)
p = (float)(c / l) * 100
print(p)
# pAlindrom in strings
#    Test 1
a = input()
i = 0
j = len(a) - 1
is_palindrom = True
while i < j:
    if a[i] != a[j]:
        is_palindrom = False
        break
    i += 1
    j -= 1
if is_palindrom:
    print("YES")
else:
    print("NO")
# Test 2
m = input()
r = m[::-1]
if m == r:
    print("Yes")
else:
    print("No")