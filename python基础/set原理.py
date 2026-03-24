class PersonHashable:
    def __init__(self, name):
        self.name = name
        print(f"执行__init__：初始化{name}")

    def __hash__(self):
        hash_val = hash(self.name)
        print(f"执行__hash__：{self.name}的哈希值={hash_val}")
        return hash_val

    def __eq__(self, other):
        # 先判断类型，再比较name
        res = isinstance(other, PersonHashable) and self.name == other.name
        print(f"执行__eq__：{self.name} vs {other.name if isinstance(other, PersonHashable) else other} → {res}")
        return res


# 阶段1：创建p3实例
p3 = PersonHashable("Alice")
# 阶段2：创建p4实例
p4 = PersonHashable("Alice")
p5 = PersonHashable("BBBB")
# 阶段3：创建集合s2（核心，处理p3和p4）   __hash__ 和__eq__在此步骤进行触发
s2 = {p3, p4,p5}
# 阶段4：输出集合长度
print(len(s2))