class QueueByList:
    def __init__(self):
        # 用列表存储队列元素
        self.queue = []

    def is_empty(self):
        """判断队列是否为空"""
        return len(self.queue) == 0

    def enqueue(self, item):
        """入队：从队尾添加元素"""
        self.queue.append(item)  # append是O(1)，高效

    def dequeue(self):
        """出队：从队首删除并返回元素"""
        if self.is_empty():
            raise IndexError("队列为空，无法出队")
        return self.queue.pop(0)  # pop(0)是O(n)，低效

    def peek(self):
        """查看队首元素（不删除）"""
        if self.is_empty():
            raise IndexError("队列为空，无队首元素")
        return self.queue[0]

    def size(self):
        """获取队列长度"""
        return len(self.queue)


# 测试列表实现的队列
if __name__ == "__main__":
    q = QueueByList()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print("队首元素：", q.peek())  # 输出：1
    print("队列长度：", q.size())  # 输出：3
    print("出队元素：", q.dequeue())  # 输出：1
    print("出队后队首：", q.peek())  # 输出：2
    print("是否为空：", q.is_empty())  # 输出：False
    q.dequeue()
    q.dequeue()
    print("是否为空：", q.is_empty())  # 输出：True