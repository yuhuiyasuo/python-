dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

# 原地合并，dict1被修改
dict1.update(dict2)
print(dict1)  # 输出: {'a': 1, 'b': 3, 'c': 4}
print(dict2)  # 输出: {'b': 3, 'c': 4}（无变化）


#-------------------------

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
# 创建新字典，原字典不变
new_dict = {**dict1, **dict2}
print(new_dict)  # 输出: {'a': 1, 'b': 3, 'c': 4}
print(dict1)     # 输出: {'a': 1, 'b': 2}（无变化）
print(dict2)     # 输出: {'b': 3, 'c': 4}（无变化）


#-------------------------
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

# 方式1：创建新字典
new_dict = dict1 | dict2
print(new_dict)  # 输出: {'a': 1, 'b': 3, 'c': 4}

# 方式2：原地合并（修改dict1）
dict1 |= dict2
print(dict1)     # 输出: {'a': 1, 'b': 3, 'c': 4}