def fun():
    return [lambda x: i*x for i in range(4)]

print(fun())

print([m(100) for m in fun()])



def fun1():
    return [lambda x, i=i: i*x for i in range(4)]

print(fun1())

print([m(100) for m in fun1()])


def fun2():
    def make_lambda(i):
        return lambda x: i*x
    return [make_lambda(i) for i in range(4)]


print(fun2())

print([m(100) for m in fun2()])