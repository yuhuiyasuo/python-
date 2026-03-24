class MinHeap:
    def __init__(self):
        # 用列表存储堆元素，索引从0开始
        self.heap = []

    def _parent(self, idx):
        """获取父节点的索引"""
        return (idx - 1) // 2

    def _left_child(self, idx):
        """获取左子节点的索引"""
        return 2 * idx + 1

    def _right_child(self, idx):
        """获取右子节点的索引"""
        return 2 * idx + 2

    def _sift_up(self, idx):
        """上浮操作：将指定索引的元素向上移动，维护小顶堆特性"""
        # 如果当前节点比父节点小，交换位置，继续上浮
        parent_idx = self._parent(idx)
        if idx > 0 and self.heap[idx] < self.heap[parent_idx]:
            self.heap[idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[idx]
            self._sift_up(parent_idx)  # 递归上浮父节点

    def _sift_down(self, idx):
        """下沉操作：将指定索引的元素向下移动，维护小顶堆特性"""
        min_idx = idx  # 初始化最小值索引为当前节点
        left_idx = self._left_child(idx)
        right_idx = self._right_child(idx)

        # 找到当前节点、左子、右子中的最小值索引
        if left_idx < len(self.heap) and self.heap[left_idx] < self.heap[min_idx]:
            min_idx = left_idx
        if right_idx < len(self.heap) and self.heap[right_idx] < self.heap[min_idx]:
            min_idx = right_idx

        # 如果最小值不是当前节点，交换并继续下沉
        if min_idx != idx:
            self.heap[idx], self.heap[min_idx] = self.heap[min_idx], self.heap[idx]
            self._sift_down(min_idx)

    def push(self, val):
        """插入元素：先加到列表末尾，再上浮"""
        self.heap.append(val)
        self._sift_up(len(self.heap) - 1)

    def pop(self):
        """弹出最小值：交换根节点和最后一个节点，删除最后一个节点，再下沉根节点"""
        if len(self.heap) == 0:
            raise IndexError("堆为空，无法弹出元素")
        # 交换根（最小值）和最后一个元素
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        min_val = self.heap.pop()  # 删除最后一个元素（原根节点）
        self._sift_down(0)  # 下沉新的根节点
        return min_val

    def peek(self):
        """获取最小值（不弹出）"""
        if len(self.heap) == 0:
            raise IndexError("堆为空")
        return self.heap[0]

    def size(self):
        """获取堆的大小"""
        return len(self.heap)


# 测试手动实现的小顶堆
heap = MinHeap()
heap.push(5)
heap.push(2)
heap.push(8)
heap.push(1)
print("手动实现的小顶堆：", heap.heap)  # 输出：[1, 2, 8, 5]
print("获取最小值：", heap.peek())  # 输出：1
print("弹出最小值：", heap.pop())  # 输出：1
print("弹出后的堆：", heap.heap)  # 输出：[2, 5, 8]