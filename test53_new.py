class Dog:
    def __new__(cls):
        print('new')
        return object.__new__(cls)
        # object.__new__()方法返回的就是实例对象的引用
        # 我们在重写的__new__()中也return 这个引用

    def __init__(self):
        print('init')


dog = Dog()