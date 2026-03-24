class ListNode:
    """双向链表节点类"""

    def __init__(self, key: int = 0, value: int = 0):
        self.key = key  # 缓存键（删除时需通过键删除哈希表中的对应项）
        self.value = value  # 缓存值
        self.prev = None  # 前驱节点
        self.next = None  # 后继节点


class LRUCache:
    def __init__(self, capacity: int):
        """
        初始化LRU缓存
        :param capacity: 缓存最大容量
        """
        self.capacity = capacity  # 缓存最大容量
        self.cache = dict()  # 哈希表：{key: ListNode}，O(1)查询节点
        self.size = 0  # 当前缓存节点数量

        # 初始化虚拟头节点和虚拟尾节点，简化边界处理
        self.dummy_head = ListNode()
        self.dummy_tail = ListNode()
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head

    def _add_node_to_tail(self, node: ListNode) -> None:
        """辅助方法：将节点添加到双向链表的尾部（标记为「最近使用」）"""
        # 1. 绑定节点的前驱和后继
        node.prev = self.dummy_tail.prev
        node.next = self.dummy_tail
        # 2. 绑定尾节点前驱的后继 和 尾节点的前驱
        self.dummy_tail.prev.next = node
        self.dummy_tail.prev = node

    def _remove_node(self, node: ListNode) -> None:
        """辅助方法：从双向链表中删除指定节点"""
        # 跳过当前节点，直接绑定前驱和后继
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _move_node_to_tail(self, node: ListNode) -> None:
        """辅助方法：将节点移到双向链表尾部（标记为「最近使用」）"""
        # 先删除节点，再添加到尾部
        self._remove_node(node)
        self._add_node_to_tail(node)

    def _pop_head_node(self) -> ListNode:
        """辅助方法：删除并返回双向链表的头节点（「最近最少使用」的节点）"""
        head_node = self.dummy_head.next
        self._remove_node(head_node)
        return head_node

    def get(self, key: int) -> int:
        """
        获取缓存值
        :param key: 要查询的键
        :return: 对应的缓存值（不存在返回-1）
        """
        if key not in self.cache:
            return -1

        # 存在：获取节点，移到尾部（标记为最近使用），返回值
        node = self.cache[key]
        self._move_node_to_tail(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        """
        添加/更新缓存
        :param key: 缓存键
        :param value: 缓存值
        """
        if key not in self.cache:
            # 情况1：键不存在，创建新节点
            new_node = ListNode(key, value)
            self.cache[key] = new_node  # 哈希表添加映射
            self._add_node_to_tail(new_node)  # 链表尾部添加节点
            self.size += 1  # 当前容量+1

            # 缓存已满，淘汰最近最少使用的节点（链表头节点）
            if self.size > self.capacity:
                removed_node = self._pop_head_node()
                del self.cache[removed_node.key]  # 删除哈希表中的对应项
                self.size -= 1  # 当前容量-1
        else:
            # 情况2：键已存在，更新值并移到尾部（标记为最近使用）
            node = self.cache[key]
            node.value = value
            self._move_node_to_tail(node)


# 测试LRUCache功能（与方式一测试用例一致）
if __name__ == "__main__":
    lru_cache = LRUCache(2)
    lru_cache.put(1, 1)
    lru_cache.put(2, 2)
    print(lru_cache.get(1))
    lru_cache.put(3, 3)
    print(lru_cache.get(2))
    lru_cache.put(4, 4)
    print(lru_cache.get(1))
    print(lru_cache.get(3))
    print(lru_cache.get(4))