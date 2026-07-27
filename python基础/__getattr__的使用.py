
# `__getattr__(self, name)` 是**实例钩子方法**
# 触发条件：
# 当使用 `obj.xxx` 访问属性时：
#
# 1. 先查找实例自身属性 → 找不到
# 2. 再查找类属性、父类属性 → 依旧找不到
# 3. **才会调用 `__getattr__(self, "xxx")`**



# ### 1. `__getattr__`
#
# **找不到属性才执行**，安全，日常动态代理首选。
#
# ### 2. `__getattribute__(self, name)`
#
# **每次执行 obj.xxx 都会无条件调用**（无论属性是否存在）

class DataWrapper:
    def __init__(self, data):
        self._data = data

    def __getattr__(self, name):
        # 属性不存在时，去内部字典查找
        if name in self._data:
            return self._data[name]
        raise AttributeError(f"对象没有属性 {name}")

d = DataWrapper({"name": "robot", "id": 1001})
print(d.name)
print(d.id)
# d.xxx 不存在会抛异常
