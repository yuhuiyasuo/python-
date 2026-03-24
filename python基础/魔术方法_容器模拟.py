class MyList:
    def __init__(self, data):
        self.data = list(data)  # 用内部列表存储数据

    # 实现__len__
    def __len__(self):
        print("触发__len__方法")
        return len(self.data)

    # 实现__getitem__（支持索引/切片）
    def __getitem__(self, key):
        print(f"触发__getitem__方法，key={key}")
        return self.data[key]  # 借助内置列表处理索引/切片

    # 实现__setitem__
    def __setitem__(self, key, val):
        print(f"触发__setitem__方法，key={key}, val={val}")
        self.data[key] = val

    # 实现__delitem__
    def __delitem__(self, key):
        print(f"触发__delitem__方法，key={key}")
        del self.data[key]

    # 实现__contains__
    def __contains__(self, item):
        print(f"触发__contains__方法，item={item}")
        return item in self.data

# 创建自定义列表实例
my_list = MyList([1, 2, 3, 4])

# 测试__len__
print("容器长度：", len(my_list))  # 触发__len__ → 输出“容器长度：4”

# 测试__getitem__（索引）
print("索引1的元素：", my_list[1])  # 触发__getitem__ → 输出“索引1的元素：2”

# 测试__getitem__（切片）
print("切片1:3的元素：", my_list[1:3])  # 触发__getitem__ → 输出“切片1:3的元素：[2, 3]”

# 测试__setitem__
my_list[2] = 10  # 触发__setitem__ → 内部data变为[1,2,10,4]
print("赋值后的容器：", my_list.data)

# 测试__delitem__
del my_list[3]  # 触发__delitem__ → 内部data变为[1,2,10]
print("删除后的容器：", my_list.data)

# 测试__contains__
print("10是否存在：", 10 in my_list)  # 触发__contains__ → 输出True