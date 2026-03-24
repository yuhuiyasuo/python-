# 通用示例
#-------------------in  not in--------------
print(2 in [1,2,3])        # True（列表）
print("key" not in {"key":1}) # False（字典，默认查键）
print(4 not in {1,2,3})    # True（集合）
print("ab" in "abc")       # True（字符串）

#-------------list
# 列表查找示例
lst = [1, 2, 3, 2, 4]

# 1. 存在性判断
print(2 in lst)  # True

# 2. 位置查找（第一个匹配）
print(lst.index(2))          # 1
print(lst.index(2, 2))       # 3（从索引2开始找）
# print(lst.index(5))        # ValueError: 5 is not in list

# 3. 统计次数
print(lst.count(2))  # 2

# 4. 条件过滤（找所有>2的元素）
print([x for x in lst if x > 2])  # [3,4]

# 5. 带索引查找（找值为2的所有索引）
print([idx for idx, val in enumerate(lst) if val == 2])  # [1,3]

#---------------------string

s = "Hello Python Python"

# 1. 子串存在性
print("Python" in s)  # True

# 2. 查找子串位置（find 不报错）
print(s.find("Python"))  # 6
print(s.find("Python",7))  # 13
print(s.find("Java"))    # -1

# 3. index 报错示例
print(s.index("Hello"))  # 0
# print(s.index("Java"))  # ValueError

# 4. 反向查找
print(s.rfind("o"))  # 10

# 5. 首尾匹配
print(s.startswith("Hello"))  # True
print(s.endswith("n"))        # True
print(s.count("Python"))   #2

#---------dict

d = {"name": "Tom", "age": 18, "gender": "male"}

# 1. 查键（核心，效率最高）
print("age" in d)          # True
print("height" not in d)   # True

# 2. 查值（安全方式：get）
print(d.get("name"))       # Tom
print(d.get("height", 180)) # 180（默认值）
# print(d["height"])        # KeyError

# 3. 查值是否存在（效率低）
print(18 in d.values())    # True

# 4. 筛选键值对（找值>10的）
print([(k, v) for k, v in d.items() if isinstance(v,int) and v > 10])  # [('age', 18)]


