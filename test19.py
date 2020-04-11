def raisetest():
    for i in range(5):
        try:
            if i == 2:
                raise NameError
        except NameError:
            print('r')
        print(i)
raisetest()