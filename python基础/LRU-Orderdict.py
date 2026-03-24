from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int):
        """
        初始化LRU缓存
        :param capacity: 缓存最大容量
        """
        self.capacity = capacity  # 缓存最大容量
        self.cache = OrderedDict()  # 有序字典，存储缓存数据，维护使用顺序

    def get(self, key: int) -> int:
        """
        获取缓存值
        :param key: 要查询的键
        :return: 对应的缓存值（不存在返回-1）
        """
        if key not in self.cache:
            return -1

        # 存在：将该键值对移到末尾，标记为「最近使用」
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        """
        添加/更新缓存
        :param key: 缓存键
        :param value: 缓存值
        """
        # 情况1：键已存在，更新值并标记为「最近使用」
        if key in self.cache:
            self.cache[key] = value
            self.cache.move_to_end(key)
            return

        # 情况2：键不存在，先判断缓存是否已满
        if len(self.cache) >= self.capacity:
            # 缓存已满：删除最前面的键值对（最近最少使用）
            self.cache.popitem(last=False)

        # 新增键值对（自动添加到末尾，标记为「最近使用」）
        self.cache[key] = value


# 测试LRUCache功能
if __name__ == "__main__":
    # 初始化容量为2的LRU缓存
    lru_cache = LRUCache(2)

    # 执行一系列操作
    lru_cache.put(1, 1)  # 缓存：{1:1}（最近使用：1）
    lru_cache.put(2, 2)  # 缓存：{1:1, 2:2}（最近使用：2）
    print(lru_cache.get(1))  # 返回1，缓存：{2:2, 1:1}（最近使用：1）
    lru_cache.put(3, 3)  # 容量满，淘汰最少使用的2，缓存：{1:1, 3:3}（最近使用：3）
    print(lru_cache.get(2))  # 返回-1（已被淘汰）
    lru_cache.put(4, 4)  # 容量满，淘汰最少使用的1，缓存：{3:3, 4:4}（最近使用：4）
    print(lru_cache.get(1))  # 返回-1（已被淘汰）
    print(lru_cache.get(3))  # 返回3，缓存：{4:4, 3:3}（最近使用：3）
    print(lru_cache.get(4))  # 返回4，缓存：{3:3, 4:4}（最近使用：4）