import math
class j:
    def __init__(self):
        self.a=1
    def __next__(self):
        self.a+=1
        if math.sqrt(self.a+100).is_integer() and math.sqrt(self.a+268).is_integer():
           print(self.a)
        else:
           return self.a
    def __iter__(self):
        return self
f=j()

print(list(f))
