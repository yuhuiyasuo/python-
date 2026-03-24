class MyRangeIterator:
    """自定义范围迭代器"""
    def __init__(self, start, end):
        # 初始化迭代的起始值、结束值、当前值
        self.start = start    # 迭代起始值
        self.end = end        # 迭代结束值（不包含）
        self.current = start  # 当前迭代位置

    # 【核心魔法方法1】返回迭代器自身（满足可迭代协议）
    def __iter__(self):
        print("触发__iter__：返回迭代器自身")
        return self

    # 【核心魔法方法2】返回下一个元素（满足迭代器协议）
    def __next__(self):
        print(f"触发__next__：当前值={self.current}")
        # 1. 判断是否还有下一个元素
        if self.current < self.end:
            # 2. 保存当前值（避免自增后返回错误值）
            res = self.current
            # 3. 迭代指针后移
            self.current += 1
            # 4. 返回当前值
            return res
        # 5. 无元素时抛出StopIteration，终止迭代
        else:
            raise StopIteration("迭代结束：已无更多元素")

# ------------------- 使用迭代器 -------------------
# 1. 创建迭代器对象
my_iter = MyRangeIterator(1, 4)  # 迭代范围：1,2,3
# 2. 方式1：用for循环遍历（自动调用__iter__和__next__）
print("===== for循环遍历 =====")
for num in my_iter:
    print(f"遍历到：{num}")

# 3. 方式2：手动调用next()（迭代器耗尽后无法复用）
print("\n===== 手动调用next() =====")
# 注意：上面的for循环已耗尽迭代器，需重新创建
new_iter = MyRangeIterator(1, 4)
print(next(new_iter))  # 1
print(next(new_iter))  # 2
print(next(new_iter))  # 3
# print(next(new_iter))  # 抛出StopIteration（无元素）