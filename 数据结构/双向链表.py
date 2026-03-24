# 定义双向链表节点类
class Node:
    def __init__(self, value):
        self.value = value  # 节点存储的值
        self.prev = None  # 前驱指针，指向前一个节点
        self.next = None  # 后继指针，指向后一个节点


# 定义双向链表类
class DoublyLinkedList:
    def __init__(self):
        self.head = None  # 头节点
        self.tail = None  # 尾节点（优化：直接维护尾节点，尾插无需遍历）
        self.size = 0  # 链表长度，避免每次遍历统计

    def is_empty(self):
        """判断链表是否为空"""
        return self.size == 0

    def forward_traverse(self):
        """正向遍历：从头节点到尾节点"""
        if self.is_empty():
            print("双向链表为空")
            return []
        current = self.head
        result = []
        while current:
            result.append(str(current.value))
            current = current.next
        print("正向遍历<->".join(result))
        return result

    def backward_traverse(self):
        """反向遍历：从尾节点到头节点"""
        if self.is_empty():
            print("双向链表为空")
            return []
        current = self.tail
        result = []
        while current:
            result.append(str(current.value))
            current = current.prev
        print("反向遍历<->".join(result))
        return result

    def add_at_head(self, value):
        """头插法：在链表头部插入新节点"""
        new_node = Node(value)
        if self.is_empty():
            # 空链表：头/尾节点都指向新节点
            self.head = new_node
            self.tail = new_node
        else:
            # 非空：新节点的next指向原头节点，原头节点的prev指向新节点，更新头节点
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def add_at_tail(self, value):
        """尾插法：在链表尾部插入新节点（无需遍历，直接用tail）"""
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            # 非空：新节点的prev指向原尾节点，原尾节点的next指向新节点，更新尾节点
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def get_node(self, index):
        """根据索引获取节点（优化：根据索引位置选择正向/反向遍历）"""
        if index < 0 or index >= self.size:
            return None  # 索引越界返回None
        # 前半段：正向遍历（更高效）
        if index < self.size // 2:
            current = self.head
            for _ in range(index):
                current = current.next
        # 后半段：反向遍历（更高效）
        else:
            current = self.tail
            for _ in range(self.size - 1 - index):
                current = current.prev
        return current

    def insert(self, index, value):
        """指定索引插入节点（索引从0开始）"""
        if index < 0 or index > self.size:
            raise IndexError("插入位置超出链表范围")
        # 索引0：头插
        if index == 0:
            self.add_at_head(value)
            return
        # 索引等于长度：尾插
        if index == self.size:
            self.add_at_tail(value)
            return
        # 中间位置插入
        new_node = Node(value)
        target_node = self.get_node(index)  # 找到要插入位置的节点
        prev_node = target_node.prev  # 插入位置的前驱节点

        # 维护前驱/后继指针
        prev_node.next = new_node
        new_node.prev = prev_node
        new_node.next = target_node
        target_node.prev = new_node
        self.size += 1

    def remove(self, value):
        """删除第一个值为value的节点"""
        if self.is_empty():
            raise ValueError("链表为空，无法删除")

        current = self.head
        while current:
            if current.value == value:
                # 找到目标节点，分3种情况处理
                prev_node = current.prev
                next_node = current.next

                # 情况1：删除头节点
                if prev_node is None:
                    self.head = next_node
                    if next_node:  # 若链表不止一个节点，更新新头节点的prev
                        next_node.prev = None
                    else:  # 删完头节点后链表为空，更新tail
                        self.tail = None
                # 情况2：删除尾节点
                elif next_node is None:
                    self.tail = prev_node
                    prev_node.next = None
                # 情况3：删除中间节点
                else:
                    prev_node.next = next_node
                    next_node.prev = prev_node

                self.size -= 1
                return  # 找到并删除后直接返回

            current = current.next

        # 遍历完未找到目标值
        raise ValueError(f"链表中不存在值为{value}的节点")

    def find(self, value):
        """查找值为value的节点，返回第一个匹配的索引（无则返回-1）"""
        if self.is_empty():
            return -1
        current = self.head
        index = 0
        while current:
            if current.value == value:
                return index
            current = current.next
            index += 1
        return -1


# 测试双向链表功能
if __name__ == "__main__":
    # 初始化链表
    dll = DoublyLinkedList()

    # 测试头插/尾插
    dll.add_at_head(2)
    dll.add_at_head(1)
    dll.add_at_tail(3)
    dll.add_at_tail(4)
    print("初始链表长度：", dll.size)  # 输出：4
    dll.forward_traverse()  # 输出：正向遍历：1<->2<->3<->4
    dll.backward_traverse()  # 输出：反向遍历：4<->3<->2<->1

    # 测试指定位置插入
    dll.insert(2, 99)
    print("\n插入99后长度：", dll.size)  # 输出：5
    dll.forward_traverse()  # 输出：正向遍历：1<->2<->99<->3<->4

    # 测试查找
    print("\n查找99的索引：", dll.find(99))  # 输出：2
    print("查找100的索引：", dll.find(100))  # 输出：-1

    # 测试删除
    dll.remove(99)  # 删除中间节点
    print("\n删除99后：")
    dll.forward_traverse()  # 输出：正向遍历：1<->2<->3<->4
    dll.remove(1)  # 删除头节点
    print("删除1后：")
    dll.forward_traverse()  # 输出：正向遍历：2<->3<->4
    dll.remove(4)  # 删除尾节点
    print("删除4后：")
    dll.forward_traverse()  # 输出：正向遍历：2<->3
    print("反向遍历：")
    dll.backward_traverse()  # 输出：反向遍历：3<->2