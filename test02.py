class Rectangle:
    def __init__(self):
        self.width = 0
        self.h=0

    def set_size(self, size):
        size=self.width,self.h

    def get_size(self):
        return self.width, self.h

    size = property(get_size, set_size)

r=Rectangle()
r.size=(150,100)

