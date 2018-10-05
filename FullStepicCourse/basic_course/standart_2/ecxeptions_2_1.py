"""
Вашей программе будет доступна функция foo, которая может бросать исключения.
Вам необходимо написать код, который запускает эту функцию, затем ловит исключения ArithmeticError,
AssertionError, ZeroDivisionError и выводит имя пойманного исключения.
"""
try:
    foo()
except ZeroDivisionError:
    print("ZeroDivisionError")
except ArithmeticError:
    print("ArithmeticError")
except AssertionError:
    print("AssertionError")


"""
напишите программу, которая будет определять обработку каких исключений можно удалить из кода.
Выведите в отдельной строке имя каждого исключения, обработку которого можно удалить из кода,
не изменив при этом поведение программы. Имена следует выводить в том же порядке, в котором они
идут во входных данных.
"""

exceptions = {}
processedExceptions = []

def found_path(exceptions, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in exceptions:
        return []
    for node in exceptions[start]:
        if node not in path:
            newPath = found_path(exceptions, node, end, path)
            if newPath:
                return newPath
    return []

n = int(input())
for _ in range(n):
    inputEx = input().split()
    child = inputEx[0]
    parents = inputEx[2:]
    exceptions[child] = parents

m = int(input())
for _ in range(m):
    processing = input()
    processedExceptions.append(processing)
    for processedException in processedExceptions:
        if len(found_path(exceptions, processing, processedException)) > 1:
            print(processing)
            break

"""
Реализуйте класс PositiveList, отнаследовав его от класса list, для хранения положительных целых \
чисел.Также реализуйте новое исключение NonPositiveError.
"""

class NonPositiveError(Exception):
    pass
class PositiveList(list):
    def append(self,x):
        if x<=0 :
            raise NonPositiveError
        else:
            super().append(x)
