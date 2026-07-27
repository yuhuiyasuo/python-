

class B:
    def __init__(self):
        print("B.__init__ 执行")

class A:
    def __new__(cls):
        print("A.__new__ 执行")
        # 返回 B 的实例，不是 A 的实例
        return B()

    def __init__(self):
        print("A.__init__ 执行")

a = A()
print(type(a))

# A() → 调用 A.__new__(A)
# A.__new__ 内部执行 B()
# B() 内部执行 B.__new__ + B.__init__
# A.__new__ 把 B 实例返回
# Python 检查：返回对象 isinstance(obj, A) → False
# 直接放弃调用 A.init


# Python 中所有的类实例化，最终都由元类 type 的 __call__ 方法驱动。它的伪代码逻辑如下：
# def __call__(cls, *args, **kwargs):
#     # 1. 调用类的 __new__
#     instance = cls.__new__(cls, *args, **kwargs)
#
#     # 2. 只有当返回的 instance 是当前类 cls 的实例时，才调用 __init__
#     if isinstance(instance, cls):
#         cls.__init__(instance, *args, **kwargs)
#
#     # 3. 返回该实例（无论它是不是 cls 的类型）
#     return instance


class Person:
    def __new__(cls, name, age):
        print(f"1. __new__ 执行，接收参数: {name}, {age}")
        print(f"   __new__ 中的 cls 是: {cls}")

        # 核心：必须调用父类的 __new__ 来创建真正的实例
        instance = super().__new__(cls)

        print(f"2. __new__ 创建了空实例，内存地址: {id(instance)}")
        return instance  # 返回这个实例

    def __init__(self, name, age):
        print(f"3. __init__ 执行，接收的 self 地址: {id(self)}")
        self.name = name
        self.age = age
        print(f"4. __init__ 初始化完成，name={self.name}, age={self.age}")


# 执行创建
p = Person("小明", 18)

# 输出结果：
# 1. __new__ 执行，接收参数: 小明, 18
#    __new__ 中的 cls 是: <class '__main__.Person'>
# 2. __new__ 创建了空实例，内存地址: 4398024512
# 3. __init__ 执行，接收的 self 地址: 4398024512   <-- 注意：地址和上面完全一致，证明是同一个对象
# 4. __init__ 初始化完成，name=小明, age=18