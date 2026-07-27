class MyMeta(type):
    def __new__(cls, name, bases, namespace):
        print(f"【__new__】cls(元类): {cls}")
        print(f"【__new__】name: {name}")
        print(f"【__new__】bases: {bases}")
        print(f"【__new__】namespace内容: {namespace}")
        return super().__new__(cls, name, bases, namespace)

    def __init__(self, name, bases, namespace):
        print(f"【__init__】self(刚创建的类): {self}")  # 注意这里已经是 Foo 了
        print(f"【__init__】name: {name}")
        print(f"【__init__】bases: {bases}")
        print(f"【__init__】namespace内容: {namespace}")
        super().__init__(name, bases, namespace)

    # 3. __call__：类() 实例化时触发
    def __call__(self, *args, **kwargs):
        print("MyMeta.__call__")
        instance = super().__call__(*args, **kwargs)
        return instance

# 这次在 Foo 里加点东西
class Foo(metaclass=MyMeta):
    x = 10
    def hello(self):
        pass


#f = Foo()

# 调用 MyMeta.__new__
# 元类的 __new__ 负责创建类对象本身（即 Foo 这个类的内存分配）。
# 参数：cls 是元类自身（MyMeta），name='Foo'，bases=(,)，namespace={}（空字典，因为 Foo 没有定义任何属性和方法）。
# 内部调用 super().__new__(cls, name, bases, namespace) → 实际调用 type.__new__，返回一个空的类对象（尚未初始化）。
# 打印："MyMeta.__new__"。
# 调用 MyMeta.__init__
# 元类的 __init__ 负责初始化刚刚创建好的类对象，例如设置类属性、方法等。
# 参数与 __new__ 相同（self 即上一步返回的类对象，name，bases，namespace）。
# 内部调用 super().__init__(name, bases, namespace) → 实际调用 type.__init__，完成标准类的初始化。
# 打印："MyMeta.__init__"。
# 至此，类 Foo 被成功创建，并成为 MyMeta 的一个实例。此时内存中已存在 Foo 类对象。