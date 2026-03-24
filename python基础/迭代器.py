# 1. 定义迭代器类：负责实现元素遍历逻辑（必须有__iter__()和__next__()）
class MyIterator:
    def __init__(self, data):
        self.data = data  # 接收可迭代对象的数据源
        self.index = 0    # 遍历索引指针，初始为0

    # 迭代器的__iter__()方法：返回自身
    def __iter__(self):
        return self

    # 迭代器的__next__()方法：核心遍历逻辑，逐个返回元素
    def __next__(self):
        # 判断索引是否越界（元素是否耗尽）
        if self.index < len(self.data):
            value = self.data[self.index]
            self.index += 1  # 索引指针后移
            return value
        # 元素耗尽，抛出StopIteration异常，终止遍历
        raise StopIteration

# 2. 定义可迭代类：负责提供迭代器（实现__iter__()方法）
class MyIterable:
    def __init__(self, data):
        self.data = data  # 存储数据源

    # 可迭代对象的核心方法：返回迭代器对象
    def __iter__(self):
        # 返回自定义迭代器的实例，传入数据源
        return MyIterator(self.data)

# 3. 测试：遍历自定义可迭代对象
if __name__ == "__main__":
    # 创建可迭代对象
    my_iterable = MyIterable([10, 20, 30, 40])

    # for循环底层自动执行iter()和next()逻辑
    for item in my_iterable:
        print(item, end=" ")  # 输出：10 20 30 40

    # 手动模拟底层流程（验证逻辑）
    print("\n--- 手动模拟底层流程 ---")
    # 步骤1：调用iter()，获取迭代器（本质调用my_iterable.__iter__()）
    iterator = iter(my_iterable)
    # 步骤2：调用next()，逐个获取元素（本质调用iterator.__next__()）
    print(next(iterator))  # 10
    print(next(iterator))  # 20
    print(next(iterator))  # 30
    print(next(iterator))  # 40
    # 步骤3：元素耗尽，next()抛出StopIteration
    # print(next(iterator))  # 报错：StopIteration