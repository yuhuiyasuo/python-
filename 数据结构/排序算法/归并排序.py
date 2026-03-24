def merge_sort(arr):
    # 基线条件：数组长度≤1时，直接返回（已有序）
    if len(arr) <= 1:
        return arr.copy()  # 返回副本，避免修改原数组

    # 1. 分：将数组拆分为左右两半
    mid = len(arr) // 2  # 取中间索引
    left_arr = merge_sort(arr[:mid])  # 递归排序左半部分
    right_arr = merge_sort(arr[mid:])  # 递归排序右半部分

    # 2. 合：合并两个有序子数组
    return merge(left_arr, right_arr)

def merge(left, right):
    merged = []  # 存储合并后的结果
    i = j = 0  # 双指针，分别遍历左、右数组

    # 步骤1：逐个比较左右数组元素，取较小值加入结果
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # 步骤2：处理剩余元素（左/右数组可能有未遍历完的元素）
    merged.extend(left[i:])  # 追加左数组剩余元素
    merged.extend(right[j:])  # 追加右数组剩余元素

    return merged

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
        sorted_arr = merge_sort(case)
        print(f"测试用例{idx + 1}：")
        print(f"原数组：{case}")
        print(f"排序后：{sorted_arr}\n")