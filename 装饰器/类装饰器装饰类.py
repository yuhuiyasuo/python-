class AddInfoDecorator:
    def __init__(self, cls):
        print("add初始化")
        self.cls = cls  # 保存被装饰的类

    def __call__(self, *args, **kwargs):
        # 实例化被装饰的类
        print("call")
        instance = self.cls(*args, **kwargs)

        # 动态添加方法
        def print_info():
            print(f"类名：{self.cls.__name__}，实例属性：{instance.__dict__}")

        instance.print_info = print_info
        print(instance.print_info)
        return instance


# 装饰类
@AddInfoDecorator
class Person:
    def __init__(self, name, age):
        print("per初始化")
        self.name = name
        self.age = age


# 创建实例并调用新增方法
p = Person("Alice", 25)
p.print_info()  # 输出：类名：Person，实例属性：{'name': 'Alice', 'age': 25}