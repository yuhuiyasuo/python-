# 普通字符串：\n 会被解析为换行
normal_str = "C:\new_folder\test.txt"
print(normal_str)
# 输出（\n 变成换行，路径错乱）：
# C:
# ew_folder	est.txt

# 原始字符串：r 前缀忽略转义，原样输出
raw_str = r"C:\new_folder\test.txt"
print(raw_str)
# 输出：C:\new_folder\test.txt

# 1. 嵌入变量
name = "张三"
age = 20
f_str1 = f"姓名：{name}，年龄：{age}"
print(f_str1)  # 输出：姓名：张三，年龄：20

# 2. 嵌入表达式
f_str2 = f"1+2的结果：{1+2}"
print(f_str2)  # 输出：1+2的结果：3

# 3. 格式化数值（保留小数、指定长度等）
score = 95.567
f_str3 = f"分数：{score:.2f}"  # .2f 保留2位小数
print(f_str3)  # 输出：分数：95.57

# 4. 嵌入字典/函数
person = {"name": "李四", "age": 22}
f_str4 = f"姓名：{person['name']}，年龄：{person['age']}"
print(f_str4)  # 输出：姓名：李四，年龄：22

# 嵌入函数调用
def add(a, b):
    return a + b
f_str5 = f"3+4={add(3,4)}"
print(f_str5)  # 输出：3+4=7


num1 = 1234.5678
print("保留2位小数：{:.2f}".format(num1))  # 1234.57
print("百分比：{:.1%}".format(0.789))      # 78.9%
print("千分位分隔：{:,}".format(123456))   # 123,456
print("整数补零：{:05d}".format(99))       # 00099