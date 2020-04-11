class a:
    def __init__(self):
        self.a=0
        b = self.a
    def __next__(self):
        b = self.a
        b=b+1
        return b
    def __iter__(self):
        return self
c=a()
for i in c:
    if i<100:
      print(i)