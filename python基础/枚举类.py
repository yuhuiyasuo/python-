from enum import Enum

# 定义枚举类（继承 Enum）
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

# 访问枚举成员
print(Color.RED)          # 输出：Color.RED
print(Color.RED.name)     # 输出：RED（成员名称）
print(Color.RED.value)    # 输出：1（成员值）

# 通过值反向查找成员
print(Color(2))           # 输出：Color.GREEN
print(Color["BLUE"])      # 输出：Color.BLUE

# 遍历所有成员
for color in Color:
    print(color.name, color.value)
# 输出：
# RED 1
# GREEN 2
# BLUE 3