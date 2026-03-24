d = {"b": 2, "a": 1, "c": 3}
# 按键升序（默认）
sorted_keys_asc = sorted(d)  # 等价于 sorted(d.keys())
print(sorted_keys_asc)  # ['a', 'b', 'c']

# 按键降序
sorted_keys_desc = sorted(d, reverse=True)
print(sorted_keys_desc)  # ['c', 'b', 'a']



#---------------------
d = {"b": 2, "a": 1, "c": 3}
# 1. 按键升序，返回(键,值)列表
sorted_items_by_key = sorted(d.items(), key=lambda x: x[0])
print(sorted_items_by_key)  # [('a', 1), ('b', 2), ('c', 3)]

# 2. 按键降序，转成有序字典（3.7+ 直接用 dict()）
sorted_dict_by_key = dict(sorted(d.items(), key=lambda x: x[0], reverse=True))
print(sorted_dict_by_key)  # {'c': 3, 'b': 2, 'a': 1}



#---------------------
d = {"b": 5, "a": 3, "c": 1, "d": 5}
# 1. 按值升序
sorted_items_by_val_asc = sorted(d.items(), key=lambda x: x[1])
print(sorted_items_by_val_asc)  # [('c', 1), ('a', 3), ('b', 5), ('d', 5)]

# 2. 按值降序
sorted_items_by_val_desc = sorted(d.items(), key=lambda x: x[1], reverse=True)
print(sorted_items_by_val_desc)  # [('b', 5), ('d', 5), ('a', 3), ('c', 1)]

# 3. 转成有序字典
sorted_dict_by_val = dict(sorted_items_by_val_asc)
print(sorted_dict_by_val)  # {'c': 1, 'a': 3, 'b': 5, 'd': 5}


#---------------------
# 示例1：值为字符串，按字母序排序
d_str = {"apple": "c", "banana": "a", "orange": "b"}
sorted_str = sorted(d_str.items(), key=lambda x: x[1])
print(sorted_str)  # [('banana', 'a'), ('orange', 'b'), ('apple', 'c')]

# 示例2：值为嵌套字典，按子字典的"age"排序
d_nest = {
    "tom": {"age": 20, "score": 90},
    "jerry": {"age": 18, "score": 85},
    "mike": {"age": 20, "score": 95}
}
# 先按子字典的age升序，age相同按score降序
sorted_nest = sorted(d_nest.items(), key=lambda x: (x[1]["age"], -x[1]["score"]))
print(sorted_nest)
# [('jerry', {'age': 18, 'score': 85}), ('mike', {'age': 20, 'score': 95}), ('tom', {'age': 20, 'score': 90})]