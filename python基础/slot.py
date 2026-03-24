from pympler import asizeof

class NormalPerson:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class SlotsPerson:
    __slots__ = ("name", "age")
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 创建 10000 个实例
normal_list = [NormalPerson(f"小明{i}", 18) for i in range(10000)]
slots_list = [SlotsPerson(f"小明{i}", 18) for i in range(10000)]

# 打印内存占用（单位：字节）
print(f"普通类实例总内存：{asizeof.asizeof(normal_list)}")  # 约 1.2MB
print(f"Slots类实例总内存：{asizeof.asizeof(slots_list)}")  # 约 0.4MB（减少 2/3）