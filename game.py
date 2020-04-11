import random
def game():
    a=random.randrange(1,7)
    b=random.randrange(1,7)
    c=random.randrange(1,7)
    num=a+b+c
    d=input('Big or Small:')

    if d in 'Big' and num>=11:
        print(str([a, b, c])+'your win')
    elif d in 'Small' and num<=10:
        print(str([a, b, c])+'your win' )
    else:
        print(str([a, b, c])+'your lose' )

print(game())
