class CircularQueue:
    def __init__(self, capacity):
        """初始化循环队列，capacity为队列总容量（含预留空位）"""
        self.capacity = capacity  # 队列总容量（比如capacity=5，实际最多存4个元素）
        self.queue = [None] * capacity  # 存储元素的固定大小数组
        self.front = 0  # 队首指针：指向第一个元素
        self.rear = 0  # 队尾指针：指向最后一个元素的下一个空位

    def is_empty(self):
        """判断队列是否为空"""
        return self.front == self.rear

    def is_full(self):
        """判断队列是否已满（预留一个空位）"""
        return (self.rear + 1) % self.capacity == self.front

    def enqueue(self, item):
        """入队：将元素添加到队尾，成功返回True，失败（满）返回False"""
        if self.is_full():
            print("队列已满，无法入队")
            return False
        # 将元素放入rear位置，然后更新rear指针（循环）
        self.queue[self.rear] = item
        self.rear = (self.rear + 1) % self.capacity
        return True

    def dequeue(self):
        """出队：移除并返回队首元素，队空返回None"""
        if self.is_empty():
            print("队列为空，无法出队")
            return None
        # 取出front位置的元素，更新front指针（循环）
        item = self.queue[self.front]
        self.queue[self.front] = None  # 可选：清空该位置，便于调试
        self.front = (self.front + 1) % self.capacity
        return item

    def peek(self):
        """查看队首元素（不删除），队空返回None"""
        if self.is_empty():
            print("队列为空，无队首元素")
            return None
        return self.queue[self.front]

    def size(self):
        """获取队列中有效元素的个数"""
        return (self.rear - self.front + self.capacity) % self.capacity

    def traverse(self):
        """遍历队列，打印所有有效元素"""
        if self.is_empty():
            print("队列为空")
            return []
        result = []
        current = self.front
        # 遍历到rear前一个位置（因为rear是空位）
        while current != self.rear:
            result.append(str(self.queue[current]))
            current = (current + 1) % self.capacity
        print("循环队列元素：", " -> ".join(result))
        return result


# 测试循环队列功能
if __name__ == "__main__":
    # 初始化容量为5的循环队列（实际最多存4个元素）
    cq = CircularQueue(5)

    # 测试入队
    cq.enqueue(1)
    cq.enqueue(2)
    cq.enqueue(3)
    cq.enqueue(4)
    cq.traverse()  # 输出：循环队列元素：1 -> 2 -> 3 -> 4
    print("队列是否已满：", cq.is_full())  # 输出：True
    print("队列有效元素个数：", cq.size())  # 输出：4

    # 测试入队满的情况
    cq.enqueue(5)  # 输出：队列已满，无法入队

    # 测试出队
    print("出队元素：", cq.dequeue())  # 输出：1
    cq.traverse()  # 输出：循环队列元素：2 -> 3 -> 4
    print("队列是否已满：", cq.is_full())  # 输出：False

    # 测试复用闲置空间（循环特性）
    cq.enqueue(5)
    cq.traverse()  # 输出：循环队列元素：2 -> 3 -> 4 -> 5
    print("队列有效元素个数：", cq.size())  # 输出：4

    # 测试查看队首
    print("队首元素：", cq.peek())  # 输出：2

    # 连续出队至空
    cq.dequeue()
    cq.dequeue()
    cq.dequeue()
    cq.dequeue()
    print("队列是否为空：", cq.is_empty())  # 输出：True
    cq.traverse()  # 输出：队列为空