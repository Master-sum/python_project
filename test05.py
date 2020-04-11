class a:
    def __init__(self):
        self.a=0
        self.b=1
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a
    def __iter__(self):
        return self
z=a()
for i in z:
    if i<100:
        print(i)