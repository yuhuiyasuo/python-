from collections import deque


class QueueByDeque:
    def __init__(self):
        self.queue = deque()  # 初始化双端队列

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        """入队：队尾添加元素"""
        self.queue.append(item)

    def dequeue(self):
        """出队：队首删除并返回元素"""
        if self.is_empty():
            raise IndexError("队列为空，无法出队")
        return self.queue.popleft()  # O(1)，高效

    def peek(self):
        """查看队首元素"""
        if self.is_empty():
            raise IndexError("队列为空，无队首元素")
        return self.queue[0]

    def size(self):
        return len(self.queue)


# 测试deque实现的队列
if __name__ == "__main__":
    q = QueueByDeque()
    q.enqueue("a")
    q.enqueue("b")
    q.enqueue("c")
    print("队首元素：", q.peek())  # 输出：a
    print("出队元素：", q.dequeue())  # 输出：a
    print("队列长度：", q.size())  # 输出：2