import random
class bingo:

    def __init__(self,item):
        self._item = list(item)
        random.shuffle(self._item)
        print(self._item)

    def pick(self):
        a = self._item.pop()
        print(a)

    def __call__(self):
        return self.pick()

b = bingo(range(4))
b.pick()