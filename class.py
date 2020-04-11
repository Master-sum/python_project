class a:
    @staticmethod
    def smeth():
        print("hello world")
    @classmethod
    def cmeth(cls):
        print('12345',cls)
a.cmeth()