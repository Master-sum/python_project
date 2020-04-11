registry = []
def register(func):
    print('run r(%s)'% func)
    registry.append(func)
    return func
@register
def f():
    print('run f')

print('1221')
print('dss')
f()