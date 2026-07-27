def f(x, y, z):
    print(x, y, z)

nums = [10, 20, 30]
#*进行解包
f(*nums)
# 等价于 f(10, 20, 30)


# * 之后的所有参数，调用时必须用关键字传参，不能用位置传参
def func(name, *, age, city):
    print(name, age, city)

func("张三", age=20, city="北京")  # ✅正常
# func("张三", 20, "北京")            # ❌报错！不能位置传age、city


d = {"a": 1, "b": 2}

def func(*args):
    print(args)

func(*d)
# 等价于 func("a", "b")
# args = ('a', 'b')