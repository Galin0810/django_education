"""
Каждая копилка имеет ограниченную вместимость, которая выражается целым числом – количеством монет,
которые можно положить в копилку. Класс должен поддерживать информацию о количестве монет в копилке,
предоставлять возможность добавлять монеты в копилку и узнавать, можно ли добавить в копилку ещё
какое-то количество монет, не превышая ее вместимость.
"""
class MoneyBox:
    def __init__(self, capacity=0):
        self.capacity = capacity

    def can_add(self, v):
        if v <= self.capacity and v > 0:
            self.capacity = self.capacity - v
            return True
        else:
            print("You can`t add monet")
            return False
    def add(self, v):
        if self.can_add(v) is True:
            return print("Add is gooooooood")
        else:
            return None
pass
a = MoneyBox(6)
a.add(6)
a.add(6)

"""
Реализуйте класс Buffer, который будет накапливать в себе элементы последовательности и выводить
сумму пятерок последовательных элементов по мере их накопления.
"""

class Buffer:
    def __init__(self):
        self.tmpList = []

    def add(self, *a):
        for item in a:
            self.tmpList.append(item)
            if (len(self.tmpList)) == 5:
                print(sum(self.tmpList))
                del self.tmpList[:5]

    def get_current_part(self):
        return self.tmpList

buf = Buffer()
buf.add(1, 2, 3)
buf.get_current_part()
buf.add(4, 5, 6)
buf.add(7, 8, 9, 10)
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
buf.get_current_part()

