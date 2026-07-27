# 普通函数：返回数字、列表、字符串等数据
# 工厂函数：返回新创建的对象（实例 / 函数）


def add(a, b):
    return a + b

# 每次调用都要传两个数
print(add(1, 2))
print(add(1, 3))



#柯里化工厂函数



def adder_factory(a):          # 工厂函数，固定第一个参数
    def inner(b):              # 返回的函数只接收剩余参数
        return a + b
    return inner

add_1 = adder_factory(1)       # 生成一个“加 1”的函数
print(add_1(2))  # 输出 3
print(add_1(3))  # 输出 4