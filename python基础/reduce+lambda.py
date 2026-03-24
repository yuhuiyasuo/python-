from functools import reduce

lst = [1, 2, 3, 4, 5]
# reduce + lambda 求和：((((1+2)+3)+4)+5) = 15
result = reduce(lambda x, y: x + y, lst,4)  #初始值在最开始当作x来进行计算
print(result)  # 19

# 对比：普通循环求和
total = 0
for num in lst:
    total += num
print(total)  # 15

