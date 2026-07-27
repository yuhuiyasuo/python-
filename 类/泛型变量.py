from typing import TypeVar, Generic

# 定义泛型变量
T = TypeVar("T")

# 继承 Generic[T]，声明这是一个持有泛型 T 的类
class Stack(Generic[T]):
    def __init__(self):
        # 内部存储 T 类型的元素
        self._items: list[T] = []

    def push(self, item: T) -> None:
        """入栈：只能压入 T 类型的元素"""
        self._items.append(item)

    def pop(self) -> T:
        """出栈：返回 T 类型的元素"""
        return self._items.pop()

    def is_empty(self) -> bool:
        return len(self._items) == 0


# ========== 使用 ==========
# 1. 整数栈：T 绑定为 int
int_stack = Stack[int]()
int_stack.push(1)
int_stack.push(2)
top_num = int_stack.pop()  # top_num 被识别为 int

# 2. 字符串栈：T 绑定为 str
str_stack = Stack[str]()
str_stack.push("hello")
str_stack.push("world")
top_str = str_stack.pop()  # top_str 被识别为 str


#====================
from typing import TypeVar

# T 只能是 int 或 str，其他类型会被类型检查工具报错
T = TypeVar("T", int, str)

def concat(a: T, b: T) -> T:
    return a + b  # int 相加 / str 拼接都合法


concat(1, 2)      # ✅ 合法
concat("a", "b")  # ✅ 合法
concat(1, "b")    # ❌ 报错：两个参数类型必须一致
concat([1], [2])  # ❌ 报错：list 不在约束范围内

