class A:
    @staticmethod
    def statmeth(*args):
        return args

a = A.statmeth(122)
print(a)
a = format(1/3,'.2%')
print(a)