class Singleton:
    # 类属性，用于存储唯一的实例
    _instance = None
    con = 1

    def __new__(cls, *args, **kwargs):
        # 判断是否已经创建过实例
        if cls._instance is None:   #instance是类属性
            # 调用父类的__new__方法创建实例
            cls._instance = super().__new__(cls)
        # 返回已有的实例（无论是否新建）
        return cls._instance

    # 可选：初始化方法（仅作演示）
    def __init__(self, name):
        if not hasattr(self,"name"):    #动态检查一个对象是否拥有指定名称的属性（包括方法） 这里self表示自己这个实例对象
            self.name = name

# 测试代码
if __name__ == "__main__":
    s1 = Singleton("实例1")
    s2 = Singleton("实例2")

    # 判断两个实例是否是同一个对象（内存地址相同）
    print(s1 is s2)  # 输出：True
    print(s1.name)  # 输出：实例2（因为s2初始化时覆盖了name属性）
    print(id(s1), id(s2))  # 输出两个相同的内存地址


