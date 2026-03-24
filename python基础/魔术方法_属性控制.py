class Person:
    def __init__(self, name):
        self.name = name  # 触发__setattr__
    # 赋值属性时校验：age必须是整数且>0
    def __setattr__(self, name, val):
        if name == "age":
            if not isinstance(val, int) or val <= 0:
                raise ValueError("年龄必须是正整数")
        # 必须调用父类方法，否则会无限递归
        super().__setattr__(name, val)
    # 访问不存在的属性时返回默认值
    def __getattr__(self, name):
        return f"属性{name}不存在，默认值：None"

    def __getattribute__(self, name):
        print(f"正在访问属性：{name}")
        # 禁止访问age属性
        if name == "age":
            raise PermissionError("禁止访问age属性")
        # 调用父类方法获取属性，避免递归
        return super().__getattribute__(name)

    # 拦截属性删除
    def __delattr__(self, name):
        # 禁止删除name属性
        if name == "name":
            raise PermissionError("禁止删除name属性")
        # 调用父类方法完成删除，避免递归
        super().__delattr__(name)


p = Person("Alice")
p.age = 20  # 正常赋值
print(p.gender)  # 属性gender不存在，默认值：None（触发__getattr__）

del p.name