# 父类定义类方法
class Parent:
    class_attr = "父类类属性"

    @classmethod
    def class_func(cls):
        print(f"当前类：{cls.__name__}，类属性：{cls.class_attr}")

# 子类1：直接继承，未重写
class Child1(Parent):
    class_attr = "子类1类属性"  # 重写类属性

# 子类2：重写类方法
class Child2(Parent):
    class_attr = "子类2类属性"

    @classmethod
    def class_func(cls):
        print(f"子类2重写的类方法，当前类：{cls.__name__}，类属性：{cls.class_attr}")

# 子类3：重写后调用父类类方法
class Child3(Parent):
    class_attr = "子类3类属性"

    @classmethod
    def class_func(cls):
        super().class_func()  # 通过super()调用父类类方法（cls仍指向Child3）
        print(f"子类3扩展的逻辑，当前类：{cls.__name__}")


# 测试调用
Parent.class_func()   # 输出：当前类：Parent，类属性：父类类属性
Child1.class_func()   # 输出：当前类：Child1，类属性：子类1类属性（cls动态绑定Child1）
Child2.class_func()   # 输出：子类2重写的类方法，当前类：Child2，类属性：子类2类属性
Child3.class_func()   # 输出：当前类：Child3，类属性：子类3类属性 → 子类3扩展的逻辑，当前类：Child3