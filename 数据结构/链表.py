# 定义节点类：每个节点包含数据和指向下一个节点的引用
class Node:
    def __init__(self, value):
        self.value = value  # 节点存储的数据
        self.next = None  # 指向下一个节点的引用，初始为None


# 定义单链表类：封装链表的核心操作
class LinkedList:
    def __init__(self):
        # 头节点，初始为None（空链表）
        self.head = None

    def is_empty(self):
        """判断链表是否为空"""
        return self.head is None

    def length(self):
        """获取链表的长度（节点个数）"""
        count = 0
        current = self.head  # 从头部开始遍历
        while current:  # 只要current不是None，就继续
            count += 1
            current = current.next
        return count

    def traverse(self):
        """遍历链表，打印所有节点的值"""
        if self.is_empty():
            print("链表为空")
            return
        current = self.head
        result = []
        while current:
            result.append(str(current.value))
            current = current.next
        print("链表节点->".join(result))

    def add_at_head(self, value):
        """头插法：在链表头部插入新节点"""
        new_node = Node(value)
        new_node.next = self.head  # 新节点的next指向原头节点
        self.head = new_node  # 头节点更新为新节点

    def add_at_tail(self, value):
        """尾插法：在链表尾部插入新节点"""
        new_node = Node(value)
        if self.is_empty():  # 空链表时，新节点直接作为头节点
            self.head = new_node
            return
        # 非空时，遍历到最后一个节点
        current = self.head
        while current.next:  # 找到next为None的节点（最后一个）
            current = current.next
        current.next = new_node  # 最后一个节点的next指向新节点

    def insert(self, index, value):
        """指定位置插入节点（索引从0开始）"""
        # 处理边界：索引小于0或大于链表长度，抛出异常
        if index < 0 or index > self.length():
            raise IndexError("插入位置超出链表范围")
        # 索引为0，等价于头插法
        if index == 0:
            self.add_at_head(value)
            return
        # 其他位置：遍历到目标位置的前一个节点
        new_node = Node(value)
        current = self.head
        count = 0
        while count < index - 1:
            current = current.next
            count += 1
        # 插入：新节点的next指向当前节点的下一个节点，当前节点的next指向新节点
        new_node.next = current.next
        current.next = new_node

    def remove(self, value):
        """删除第一个值为value的节点"""
        if self.is_empty():
            raise ValueError("链表为空，无法删除")

        # 情况1：要删除的是头节点
        if self.head.value == value:
            self.head = self.head.next
            return

        # 情况2：要删除的是中间/尾部节点
        current = self.head
        # 遍历找前驱节点（current的next是要删除的节点）
        while current.next and current.next.value != value:
            current = current.next

        # 如果遍历完没找到，抛出异常
        if current.next is None:
            raise ValueError(f"链表中不存在值为{value}的节点")
        # 找到后，跳过要删除的节点（修改指针）
        current.next = current.next.next

    def find(self, value):
        """查找值为value的节点是否存在，返回布尔值"""
        if self.is_empty():
            return False
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False


# 测试链表功能
if __name__ == "__main__":
    # 初始化链表
    ll = LinkedList()

    # 测试空链表
    print("是否为空：", ll.is_empty())  # 输出：True
    ll.traverse()  # 输出：链表为空

    # 头插法插入节点
    ll.add_at_head(3)
    ll.add_at_head(2)
    ll.add_at_head(1)
    ll.traverse()  # 输出：链表节点：1->2->3

    # 尾插法插入节点
    ll.add_at_tail(4)
    ll.add_at_tail(5)
    ll.traverse()  # 输出：链表节点：1->2->3->4->5

    # 测试长度
    print("链表长度：", ll.length())  # 输出：5

    # 指定位置插入
    ll.insert(2, 99)
    ll.traverse()  # 输出：链表节点：1->2->99->3->4->5

    # 查找节点
    print("是否存在99：", ll.find(99))  # 输出：True
    print("是否存在100：", ll.find(100))  # 输出：False

    # 删除节点
    ll.remove(99)
    ll.traverse()  # 输出：链表节点：1->2->3->4->5
    ll.remove(1)  # 删除头节点
    ll.traverse()  # 输出：链表节点：2->3->4->5
    ll.remove(5)  # 删除尾节点
    ll.traverse()  # 输出：链表节点：2->3->4