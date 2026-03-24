# 父类定义静态方法
class Parent:
    @staticmethod
    def static_func():
        print("父类的静态方法")

# 子类1：直接继承，未重写
class Child1(Parent):
    pass

# 子类2：重写静态方法
class Child2(Parent):
    @staticmethod
    def static_func():
        print("子类2重写的静态方法")

# 子类3：重写后显式调用父类静态方法
class Child3(Parent):
    @staticmethod
    def static_func():
        #super().static_func()   #静态方法是不可以被继承的
        Parent.static_func()  # 显式调用父类
        print("子类3的静态方法")

# 测试调用
Child1.static_func()  # 输出：父类的静态方法
Child2.static_func()  # 输出：子类2重写的静态方法
Child3.static_func()  # 输出：父类的静态方法 → 子类3的静态方法