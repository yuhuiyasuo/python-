# 定义3个等长的可迭代对象
list1 = [1, 2, 3, 4]
list2 = ["a", "b", "c", "d"]
tuple1 = (10, 20, 30, 40)

# 调用 zip() 进行打包，返回 zip 迭代器
zip_result = zip(list1, list2, tuple1)

# 1. 查看 zip 对象（直接打印无法看到具体元素，因为是迭代器）
print("zip 对象本身：", zip_result)
print("zip 对象类型：", type(zip_result))

# 2. 转换为列表，查看打包后的具体内容（常用方式）
zip_list = list(zip_result)
print("打包后转换为列表：", zip_list)

# 3. 转换为元组，查看打包后的具体内容
zip_tuple = tuple(zip(list1, list2, tuple1))  # 重新打包（迭代器只能遍历一次）
print("打包后转换为元组：", zip_tuple)



# 定义3个长度不同的可迭代对象
list_short = [1, 2, 3]  # 最短：长度3
list_mid = ["a", "b", "c", "d"]   # 长度4
list_long = [10, 20, 30, 40, 50]  # 最长：长度5

# 打包不等长可迭代对象
zip_uneven = list(zip(list_short, list_mid, list_long))
print("不等长可迭代对象打包结果：", zip_uneven)
