class People(object):
    # 创建对象
    def __new__(cls, *args, **kwargs):
        print("触发了构造方法")
        ret = super().__new__(cls)  # 调用父类的__new__()方法创建对象
        return ret  ## 将对象返

    # 实例化对象
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("初始化方法")

    #  删除对象
    #   del 对象名或者程序执行结束之后
    def __del__(self):
        print("析构方法，删除对象")

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"

    def __repr__(self):
        return f"Person('{self.name}', {self.age})"

    def __format__(self, format_spec):
        return ' '.join([self.name, format_spec])

if __name__ == '__main__':
    p1 = People('xiaoming', 16)
    print(p1)
    print(repr(p1))
    print(format(p1, 'No.1'))

