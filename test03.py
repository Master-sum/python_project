class a:
    def __init__(self):
       self.hungry=True
    def eat(self):
        if self.hungry:
            print('AAAAA')
            self.hungry=False
        else:
            print('No thank')
class b(a):
    def __init__(self):
        super().__init__()
        self.s='1233'
    def sing(self):
        print(self.s)
sb=b()
sb.sing()
sb.eat()
sb.eat()
