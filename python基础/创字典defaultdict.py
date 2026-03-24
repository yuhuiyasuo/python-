

normal_dict = {}

# 访问存在的 key：没问题
normal_dict['a'] = 100
print(normal_dict['a'])  # 输出 100

# 访问不存在的 key：直接报错！
print(normal_dict['b'])  # KeyError: 'b'


from collections import defaultdict

# 创建一个：找不到 key 就默认返回 0 的字典

#defaultdict 要求你传入的是一个 “能被调用的东西（函数）   错误：defaultdict( 0)
in_degree = defaultdict(lambda: 0)

'''
defaultdict(int)        # 最常用，等价于 lambda:0
defaultdict(lambda: 0)  # 等价效果
defaultdict(list)       # 默认空列表
defaultdict(dict)       # 默认空字典
'''

print(in_degree['a'])  # 0 （自动给 0，不报错）
print(in_degree['b'])  # 0
print(in_degree['xxx']) # 0