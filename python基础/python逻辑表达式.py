
# 表达式：3 > 2 and 4 + 1 < 6 or not 6 == 7
# 步骤1：算术运算（4+1=5）
# 步骤2：比较运算（3>2=True；5<6=True；6==7=False）
# 步骤3：逻辑运算符（not False=True → True and True=True → True or True=True）
print(3 > 2 and 4 + 1 < 6 or not 6 == 7)  # 输出 True



# 1. not 的右结合
print(not not True)  # 等价于 not (not True) → not False → True

# 2. and 的左结合
print(1 and 0 and 2) # 等价于 (1 and 0) and 2 → 0 and 2 → 0

# 3. or 的左结合
print(0 or 1 or 2)   # 等价于 (0 or 1) or 2 → 1 or 2 → 1




# 示例1：and 短路（左为假，右不执行）
a = 0
result = a and (a := 1)  # := 是赋值表达式（Python3.8+）
print(result)  # 0（a未被重新赋值）
print(a)       # 0

# 示例2：or 短路（左为真，右不执行）
a = 1
result = a or (a := 2)
print(result)  # 1（a未被重新赋值）
print(a)       # 1

# 示例3：无短路（左无法确定结果，执行右侧）
a = 1
result = a and (a := 2)
print(result)  # 2（a被重新赋值）
print(a)       # 2