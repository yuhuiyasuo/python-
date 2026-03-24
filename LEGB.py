class Person:
    def __init__(self, name, age):
        self.name = name
        # 初始化时调用setter，触发校验
        self.age = age

    # 1. 定义getter（读取属性时触发）
    @property
    def age(self):
        # 内部用 _age 存储真实值（约定：单下划线表示私有变量）,不能使用age，否则会引发循环，self就表示实例
        print("1")
        return self._age   #写成self.age 就相当于p.age

    # 2. 定义setter（赋值属性时触发）
    @age.setter
    def age(self, value):
        # 校验逻辑：年龄必须是0-150的整数/浮点数
        if not isinstance(value, (int, float)):
            raise TypeError("年龄必须是数字")
        if value < 0 or value > 150:
            raise ValueError("年龄必须在0-150之间")
        # 校验通过，赋值给 _age
        self._age = value


# 使用示例
p = Person("李四", 25)
print(p.age)  # 读取：25（触发 @property 装饰的age方法）

p.age = 30    # 赋值：30（触发 @age.setter 装饰的age方法）
print(p.age)  # 输出：30

# 非法赋值会触发异常
# p.age = -5   # ValueError: 年龄必须在0-150之间
# p.age = "30" # TypeError: 年龄必须是数字