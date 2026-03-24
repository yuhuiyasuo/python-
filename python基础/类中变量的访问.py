class ParentLRU:  # 父类
    def __init__(self, capacity):
        self.__capacity = capacity  # 父类私有属性：改写为 _ParentLRU__capacity


class ChildLRU(ParentLRU):  # 子类
    def __init__(self, capacity):
        super().__init__(capacity)

    def get_parent_capacity(self):
        # 尝试直接访问父类私有属性：报错！
        return self.__capacity  # 子类中改写为 _ChildLRU__capacity，未定义


# 测试
child = ChildLRU(2)
#print(child.get_parent_capacity())  # AttributeError: 'ChildLRU' object has no attribute '_ChildLRU__capacity'

#==========================父类通过@property封装私有属性的访问
class ParentLRU:
    def __init__(self, capacity):
        self.__capacity = capacity  # 私有属性

    # 暴露公共的只读属性
    @property
    def capacity(self):
        return self.__capacity


class ChildLRU(ParentLRU):
    def __init__(self, capacity):
        super().__init__(capacity)

    def get_capacity(self):
        # 子类通过父类的property接口访问私有属性
        return self.capacity  # 合法！


# 测试
child = ChildLRU(2)
print(child.get_capacity())  # 2（正确访问父类私有属性）




#===========================父类定义公共 getter 方法
class ParentLRU:
    def __init__(self, capacity):
        self.__capacity = capacity

    # 公共getter方法
    def get_capacity(self):
        return self.__capacity


class ChildLRU(ParentLRU):
    def print_capacity(self):
        # 子类调用父类的公共方法
        print(f"父类私有容量：{super().get_capacity()}")


child = ChildLRU(3)
child.print_capacity()  # 父类私有容量：3