def heap_sort(arr):

    n = len(arr)
    if n <= 1:
        return  # 空数组/单元素数组无需排序

    # 步骤1：构建大顶堆（从最后一个非叶子节点向前遍历调整）
    for i in range(n // 2 - 1, -1, -1):
        sift_down(arr, n, i)

    # 步骤2：循环交换堆顶与末尾元素，调整剩余堆
    for i in range(n - 1, 0, -1):
        # 交换堆顶（最大值）与当前未排序部分的末尾
        arr[0], arr[i] = arr[i], arr[0]
        # 对剩余未排序元素（0~i-1）重新调整为大顶堆
        sift_down(arr, i, 0)


def sift_down(arr, heap_size, parent_idx):

    largest_idx = parent_idx  # 初始化最大值索引为父节点
    left_child = 2 * parent_idx + 1  # 左子节点索引
    right_child = 2 * parent_idx + 2  # 右子节点索引

    # 1. 比较父节点与左子节点，更新最大值索引
    if left_child < heap_size and arr[left_child] > arr[largest_idx]:
        largest_idx = left_child

    # 2. 比较最大值索引与右子节点，更新最大值索引
    if right_child < heap_size and arr[right_child] > arr[largest_idx]:
        largest_idx = right_child

    # 3. 如果最大值不是父节点，交换并递归调整受影响的子树
    if largest_idx != parent_idx:
        arr[parent_idx], arr[largest_idx] = arr[largest_idx], arr[parent_idx]
        # 递归调整交换后的子节点所在的子树
        sift_down(arr, heap_size, largest_idx)


# 测试用例
if __name__ == "__main__":
    # 测试不同场景：随机数组、空数组、单元素数组、已排序数组、逆序数组
    test_cases = [
        [38, 27, 43, 3, 9, 82, 10],  # 随机无序
        [],  # 空数组
        [5],  # 单元素
        [1, 2, 3, 4, 5],  # 已排序
        [5, 4, 3, 2, 1]  # 逆序
    ]

    for idx, case in enumerate(test_cases):
        # 复制数组避免修改原测试用例
        arr_copy = case.copy()
        heap_sort(arr_copy)
        print(f"测试用例{idx + 1}：")
        print(f"原数组：{case}")
        print(f"排序后：{arr_copy}\n")