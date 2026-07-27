class Meta(type):
    def __new__(mcls, name, bases, namespace):
        print("1.元类 __new__：创建类对象")
        cls = super().__new__(mcls, name, bases, namespace)
        return cls

    def __init__(cls, name, bases, namespace):
        print("2.元类 __init__：初始化类对象")
        # namespace 里面已经收集好所有【类属性代码】
        super().__init__(name, bases, namespace)

class MyClass(metaclass=Meta):
    attr_a = 100          # 类属性
    def __init__(self):
        print("4.实例 __init__：创建对象时执行")

obj = MyClass()