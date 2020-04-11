class A:
    def spam(self):
        print("A.ppp")

class B(A):
    def bar(self):
        print("B.bar")
a = A()
b = B()
b.bar()