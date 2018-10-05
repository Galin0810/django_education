"""
Напишите программу, которая считывает файл с подобной структурой и для каждого абитуриента
выводит его среднюю оценку по этим трём предметам на отдельной строке, соответствующей этому
абитуриенту. Также в конце файла, на отдельной строке, через пробел запишите средние баллы
по математике, физике и русскому языку по всем абитуриентам:
"""

count = 0
lst = []
with open('/home/galina/Downloads/dataset_3363_4.txt') as file:
    for string in file:
        string = string.strip().split(';')

        for i in string[1::]:
            count += int(i)
        print(count/3)
        string.append(count/3)

        lst.append(string)

        count = 0

math = 0
phys = 0
rus = 0
for i in lst:
    math += int(i[1])
    phys += int(i[2])
    rus += int(i[3])
print(math/len(lst), phys/len(lst), rus/len(lst))

"""

"""