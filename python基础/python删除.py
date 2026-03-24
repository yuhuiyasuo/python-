#----------del
# 示例1：删除列表元素/切片
lst = [1, 2, 3, 4]
del lst[1]          # 删索引1的元素，lst → [1,3,4]
del lst[1:3]        # 删索引1-2的元素，lst → [1]

# 示例2：删除字典键值对
d = {"name": "Tom", "age": 18}
del d["age"]        # d → {"name": "Tom"}
# del d["height"]    # KeyError: 'height'

# 示例3：删除变量
var = 10
del var
# print(var)         # NameError: name 'var' is not defined

#------------list
lst = [1, 2, 3, 2, 4]

# 1. pop（删索引+返回值）
print(lst.pop())     # 4（删最后一个），lst → [1,2,3,2]
print(lst.pop(1))    # 2（删索引1），lst → [1,3,2]
# lst.pop(10)        # IndexError: pop index out of range

# 2. remove（删第一个匹配）
lst.remove(2)        # lst → [1,3]
# lst.remove(5)      # ValueError: list.remove(x): x not in list

# 3. clear（清空）
lst.clear()          # lst → []

#------------------dict
d = {"name": "Tom", "age": 18, "gender": "male"}

# 1. pop（安全删键，带默认值）
print(d.pop("age"))         # 18，d → {"name":"Tom", "gender":"male"}
print(d.pop("height", 180)) # 180（键不存在，返回默认值）

# 2. popitem（删最后一个键值对）
print(d.popitem())          # ("gender", "male")，d → {"name":"Tom"}

# 3. clear（清空）
d.clear()                   # d → {}


#---------------set
s = {1, 2, 3, 4}

# 1. remove（删指定元素，报错风险）
s.remove(3)        # s → {1,2,4}
# s.remove(10)      # KeyError: 10

# 2. discard（安全删除）
s.discard(2)       # s → {1,4}
s.discard(10)      # 无报错，s仍为{1,4}

# 3. pop（随机删除）
print(s.pop())     # 1（随机），s → {4}

# 4. clear（清空）
s.clear()          # s → set()

