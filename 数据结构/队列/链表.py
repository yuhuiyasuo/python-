# 先定义节点类（复用之前的链表节点）
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class QueueByLinkedList:
    def __init__(self):
        self.head = None  # 队首（出队端）
        self.tail = None  # 队尾（入队端）
        self.count = 0  # 记录队列长度，避免每次遍历

    def is_empty(self):
        return self.count == 0

    def enqueue(self, item):
        """入队：队尾添加节点"""
        new_node = Node(item)
        if self.is_empty():
            # 空队列时，头和尾都指向新节点
            self.head = new_node
            self.tail = new_node
        else:
            # 非空时，尾节点的next指向新节点，更新尾节点
            self.tail.next = new_node
            self.tail = new_node
        self.count += 1

    def dequeue(self):
        """出队：队首删除节点并返回值"""
        if self.is_empty():
            raise IndexError("队列为空，无法出队")
        # 取出头节点的值
        value = self.head.value
        # 更新头节点为下一个节点
        self.head = self.head.next
        self.count -= 1
        # 如果队列为空，尾节点也要置为None
        if self.is_empty():
            self.tail = None
        return value

    def peek(self):
        """查看队首元素"""
        if self.is_empty():
            raise IndexError("队列为空，无队首元素")
        return self.head.value

    def size(self):
        return self.count


# 测试链表实现的队列
if __name__ == "__main__":
    q = QueueByLinkedList()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    print("队首元素：", q.peek())  # 输出：10
    print("出队元素：", q.dequeue())  # 输出：10
    print("队列长度：", q.size())  # 输出：2
    q.dequeue()
    q.dequeue()
    print("是否为空：", q.is_empty())  # 输出：True