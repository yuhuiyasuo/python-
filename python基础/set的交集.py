s1 = {1, 2, 3}
s2 = {2, 3, 4}

# 交集
print(s1 & s2)  # {2,3}
print(s1.intersection(s2))  # {2,3}

# 并集
print(s1 | s2)  # {1,2,3,4}
print(s1.union(s2))  # {1,2,3,4}

# 差集（s1有、s2无）
print(s1 - s2)  # {1}
print(s1.difference(s2))  # {1}

# 对称差集（s1和s2互不包含的元素）
print(s1 ^ s2)  # {1,4}
print(s1.symmetric_difference(s2))  # {1,4}