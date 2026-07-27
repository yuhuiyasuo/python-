# 通过字符串名字动态获取对象的属性或方法

class Calc:
    def add(self, a, b):
        return a + b

c = Calc()

# 获取方法对象
func = getattr(c, "add")
# 调用
print(func(3, 5))  # 8

# 一行简写
print(getattr(c, "add")(2, 4))  # 6

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("张三", 20)

# 等价于 p.name
print(getattr(p, "name"))   # 张三

# 属性不存在，不设置default → 报错
# print(getattr(p, "gender"))

# 设置default，不存在返回默认值
print(getattr(p, "gender", "未知"))  # 未知

class Handler:
    def query(self):
        print("执行查询")
    def insert(self):
        print("执行新增")

h = Handler()
action = "query"

# 动态执行
if hasattr(h, action):
    getattr(h, action)()
else:
    print("操作不存在")
