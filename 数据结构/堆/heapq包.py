import heapq

# 1. 初始化堆（两种方式）
# 方式A：空堆逐步插入
heap1 = []
heapq.heappush(heap1, 5)
heapq.heappush(heap1, 2)
heapq.heappush(heap1, 8)
heapq.heappush(heap1, 1)
print("初始化后的小顶堆：", heap1)  # 输出：[1, 2, 8, 5]（注：堆的存储是数组，但逻辑是完全二叉树）

# 方式B：将现有列表转为堆（原地修改，时间复杂度O(n)）
heap2 = [5, 2, 8, 1]
heapq.heapify(heap2)
print("heapify后的小顶堆：", heap2)  # 输出：[1, 2, 8, 5]

# 2. 获取堆的最小值（根节点）：直接取索引0，O(1)
min_val = heap1[0]
print("堆的最小值：", min_val)  # 输出：1

# 3. 弹出堆的最小值（弹出后自动维护堆结构，O(logn)）
pop_val = heapq.heappop(heap1)
print("弹出的最小值：", pop_val)  # 输出：1
print("弹出后的堆：", heap1)      # 输出：[2, 5, 8]

# 4. 弹出最小值并插入新值（等价于heappop+heappush，更高效）
heapq.heapreplace(heap1, 0)
print("替换后的堆：", heap1)      # 输出：[0, 5, 8]