# 定义二叉树节点类
class TreeNode:
    def __init__(self, value):
        self.value = value  # 节点存储的值
        self.left = None    # 左子节点引用
        self.right = None   # 右子节点引用

# 定义二叉树类
class BinaryTree:
    def __init__(self):
        self.root = None  # 根节点，初始为空

    # ---------------------- 插入节点（按二叉搜索树规则，便于演示） ----------------------
    def insert(self, value):
        """插入节点（二叉搜索树规则：左子树<根<右子树）"""
        new_node = TreeNode(value)
        # 空树：新节点作为根节点
        if self.root is None:
            self.root = new_node
            return
        # 非空树：遍历找到插入位置
        current = self.root
        while True:
            # 避免重复值
            if value == current.value:
                raise ValueError(f"值{value}已存在于二叉树中")
            # 小于当前节点：往左子树走
            elif value < current.value:
                if current.left is None:
                    current.left = new_node
                    break
                current = current.left
            # 大于当前节点：往右子树走
            else:
                if current.right is None:
                    current.right = new_node
                    break
                current = current.right

    # ---------------------- 深度优先遍历（递归实现，修复递归逻辑） ----------------------
    def pre_order_recursive(self, node=None, result=None):
        """前序遍历（递归）：根→左→右"""
        if result is None:
            result = []
        # 修复：仅初始调用（node为None）时设为root，递归调用时node为None直接返回
        if node is None:
            if self.root is None:  # 空树直接返回
                return result
            node = self.root  # 第一次调用，从根节点开始
        else:
            if node is None:  # 递归调用时node为None，直接返回
                return result
        # 正常遍历逻辑
        result.append(node.value)  # 先访问根
        if node.left:  # 左子节点不为None才递归
            self.pre_order_recursive(node.left, result)
        if node.right:  # 右子节点不为None才递归
            self.pre_order_recursive(node.right, result)
        return result

    def in_order_recursive(self, node=None, result=None):
        """中序遍历（递归）：左→根→右"""
        if result is None:
            result = []
        if node is None:
            if self.root is None:
                return result
            node = self.root
        else:
            if node is None:
                return result
        if node.left:  # 先遍历左子树
            self.in_order_recursive(node.left, result)
        result.append(node.value)  # 再访问根
        if node.right:  # 最后遍历右子树
            self.in_order_recursive(node.right, result)
        return result

    def post_order_recursive(self, node=None, result=None):
        """后序遍历（递归）：左→右→根"""
        if result is None:
            result = []
        if node is None:
            if self.root is None:
                return result
            node = self.root
        else:
            if node is None:
                return result
        if node.left:  # 先遍历左子树
            self.post_order_recursive(node.left, result)
        if node.right:  # 再遍历右子树
            self.post_order_recursive(node.right, result)
        result.append(node.value)  # 最后访问根
        return result

    # ---------------------- 深度优先遍历（迭代实现，模拟栈） ----------------------
    def pre_order_iterative(self):
        """前序遍历（迭代）：借助栈"""
        if self.root is None:
            return []
        stack = [self.root]
        result = []
        while stack:
            node = stack.pop()  # 弹出栈顶节点
            result.append(node.value)
            # 先压右子节点（栈先进后出，保证左子节点先被访问）
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result

    # ---------------------- 广度优先遍历（层序遍历，借助队列） ----------------------
    def level_order(self):
        """层序遍历：按层级访问节点"""
        if self.root is None:
            return []
        from collections import deque
        queue = deque([self.root])  # 队列存储待访问的节点
        result = []
        while queue:
            level_size = len(queue)  # 当前层级的节点数
            level_nodes = []  # 存储当前层级的节点值
            for _ in range(level_size):
                node = queue.popleft()  # 弹出队首节点
                level_nodes.append(node.value)
                # 左子节点入队
                if node.left:
                    queue.append(node.left)
                # 右子节点入队
                if node.right:
                    queue.append(node.right)
            result.append(level_nodes)
        return result

    # ---------------------- 查找节点 ----------------------
    def find(self, value):
        """查找值为value的节点，返回节点对象（None表示不存在）"""
        if self.root is None:
            return None
        current = self.root
        while current:
            if value == current.value:
                return current  # 找到，返回节点
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return None  # 未找到

    # ---------------------- 删除节点（难点：分3种情况） ----------------------
    def _find_min_node(self, node):
        """找到以node为根的子树中值最小的节点（用于删除双子节点的情况）"""
        current = node
        while current.left is not None:
            current = current.left
        return current

    def delete(self, value):
        """删除值为value的节点，返回删除后的根节点"""
        # 递归辅助函数：删除以node为根的子树中值为value的节点
        def _delete(node, value):
            if node is None:
                return None  # 未找到要删除的节点
            # 1. 找到要删除的节点
            if value < node.value:
                node.left = _delete(node.left, value)
            elif value > node.value:
                node.right = _delete(node.right, value)
            else:
                # 2. 处理删除逻辑（分3种情况）
                # 情况1：叶子节点（无左右子节点）
                if node.left is None and node.right is None:
                    return None
                # 情况2：只有一个子节点（左或右）
                elif node.left is None:
                    return node.right  # 用右子节点替换当前节点
                elif node.right is None:
                    return node.left   # 用左子节点替换当前节点
                # 情况3：有两个子节点（找右子树最小值节点替换，再删除该最小值节点）
                else:
                    min_right_node = self._find_min_node(node.right)  # 右子树最小值
                    node.value = min_right_node.value  # 替换当前节点值
                    node.right = _delete(node.right, min_right_node.value)  # 删除最小值节点
            return node

        self.root = _delete(self.root, value)

# 测试二叉树功能
if __name__ == "__main__":
    # 初始化二叉树并插入节点
    bt = BinaryTree()
    bt.insert(8)
    bt.insert(3)
    bt.insert(10)
    bt.insert(1)
    bt.insert(6)
    bt.insert(14)
    bt.insert(4)
    bt.insert(7)
    bt.insert(13)

    # 测试遍历
    print("前序遍历（递归）：", bt.pre_order_recursive())  # [8,3,1,6,4,7,10,14,13]
    print("中序遍历（递归）：", bt.in_order_recursive())    # [1,3,4,6,7,8,10,13,14]
    print("后序遍历（递归）：", bt.post_order_recursive())  # [1,4,7,6,3,13,14,10,8]
    print("前序遍历（迭代）：", bt.pre_order_iterative())  # [8,3,1,6,4,7,10,14,13]
    print("层序遍历：", bt.level_order())                  # [[8], [3,10], [1,6,14], [4,7,13]]

    # 测试查找
    print("\n查找值6的节点：", bt.find(6).value if bt.find(6) else "不存在")  # 6
    print("查找值9的节点：", bt.find(9))  # None

    # 测试删除
    bt.delete(6)  # 删除有两个子节点的节点
    print("\n删除6后中序遍历：", bt.in_order_recursive())  # [1,3,4,7,8,10,13,14]
    bt.delete(3)  # 删除有两个子节点的节点
    print("删除3后中序遍历：", bt.in_order_recursive())  # [1,4,7,8,10,13,14]
    bt.delete(14) # 删除有一个子节点的节点
    print("删除14后中序遍历：", bt.in_order_recursive()) # [1,4,7,8,10,13]
    bt.delete(1)  # 删除叶子节点
    print("删除1后中序遍历：", bt.in_order_recursive())  # [4,7,8,10,13]