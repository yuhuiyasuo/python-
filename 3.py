class AttrDemo:
    def __init__(self):
        # 用基类方法赋值，避免触发 __setattr__
        object.__setattr__(self, "_store", {})

    def __getattr__(self, name):
        """obj.xxx 找不到属性时触发"""
        print(f"【__getattr__】尝试读取不存在属性: {name}")
        if name in self._store:
            return self._store[name]
        raise AttributeError(f"{self} 对象没有属性 {name}")

    def __setattr__(self, name, value):
        """obj.xxx = value 每次都会触发"""
        print(f"【__setattr__】设置属性 {name} = {value}")
        # 区分：如果是内部私有变量直接挂载实例上，其余存入字典
        if name == "_store":
            object.__setattr__(self, name, value)
        else:
            self._store[name] = value

    def __delattr__(self, name):
        """del obj.xxx 触发"""
        print(f"【__delattr__】删除属性 {name}")
        if name in self._store:
            del self._store[name]
        else:
            raise AttributeError(f"无法删除不存在属性 {name}")


obj = AttrDemo()

# 1. 设置属性 → __setattr__
obj.name = "robot"
obj.age = 24

# 2. 读取属性
# name不在实例自身，进入__getattr__
print(obj.name)
print(obj.age)

# 3. 删除属性 → __delattr__
del obj.age

# 4. 删除后再访问 age，触发异常
# print(obj.age)
