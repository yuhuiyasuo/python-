import  re

s = "Abc12345"  # 符合；s2="abc12345" 不符合（无大写）
pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$"

res = re.match(pattern, s)
print(bool(res))  # 输出：True

#后面不是数字的字母
s = "a1 b2 c d3"
pattern = r"\w(?!\d)"
res = re.findall(pattern, s)
print(res)  # 输出：['c', '1', '2', '3']（注意：1/2/3后无字符，也满足“后面不是数字”）

#前面必须是数字的字母
s = "1a 2b c 3d"
pattern = r"(?<=\d)\w"
res = re.findall(pattern, s)
print(res)  # 输出：['a', 'b', 'd']

s = "13812345678 13998765432"
# 匹配第4-7位数字，要求前面是3位数字，后面是4位数字
pattern = r"(?<=\d{3})\d{4}(?=\d{4})"
res = re.sub(pattern, "****", s)
print(res)  # 输出：138****5678 139****5432