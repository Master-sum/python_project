def test(a):
    b = []
    for i in range(a):

        yield i

        i += 1
        b.append(i)

    print(b)

a = test(5)
print()

