file = open('/home/galina/Downloads/dataset_3363_2.txt', 'r')
file2 = open('/home/galina/Downloads/new_file.txt', 'w')
s = file.readline()
#print(s)

list = []
count = -1

for i in range(len(s)):
    if 'a' <= s[i] <= 'z':
        list.append([s[i]])
        count += 1
    elif 'A' <= s[i] <= 'Z':
        list.append([s[i]])
        count += 1
    elif '0' <= s[i] <= '9':
        list[count].append(s[i])
#print(list)

for i in range(len(list)):
    #print(list[i][1::])
    str2 = ''
    for j in list[i][1::]:
        str2 = str2 + j
        file2.write(list[i][0] * int(str2))
        file2.closed
    print(list[i][0]*int(str2), end='')
print()
