# from dataclasses import dataclass
#
# @dataclass
# class Student:
#     name: str
#     age: int
#
# # 等价于
# # class Student:
# #     def __init__(self, name: str, age: int):
# #         self.name = name
# #         self.age = age
# #
# #     def __repr__(self):
# #         return f"Student(name={self.name}, age={self.age})"
# #
# #     def __eq__(self, other):
# #         return (
# #             self.name == other.name
# #             and self.age == other.age
# #         )
#
# s1 = Student("Tom", 18)
# s2 = Student("Tom", 18)
# s3 = Student("Jerry", 20)
#
# # ✅ 使用 == ，内部自动调用 __eq__
# print(s1 == s2)   # True  所有字段全部相等
# print(s1 == s3)   # False 字段不一样
#
#
# print(s1)
#
#
# #=============================================================
# from dataclasses import dataclass, field
#
# @dataclass
# class Student:
#     scores: list = field(default_factory=list)   #list是一个函数，后续是调用

from dataclasses import dataclass, field

# ====================== 错误示例 default=[] 共享可变对象 ======================
@dataclass
class Student1:
    scores: list[int]


s1 = Student1()
s2 = Student1()

s1.scores.append(90)

print("s1.scores =", s1.scores)  # [90]
print("s2.scores =", s2.scores)  # [90] ！！！s2也被修改了，两个实例共享同一个list
print(id(s1.scores))
print(id(s2.scores))  # id完全相同，是内存中同一个对象


# ====================== 正确示例 default_factory 每次新建对象 ======================
@dataclass
class User:
    name: str
    hobbies: list[str] = field(default_factory=list)


u1 = User(name="Tom")
u2 = User(name="Jerry")

u1.hobbies.append("篮球")

print("u1.hobbies =", u1.hobbies) # ['篮球']
print("u2.hobbies =", u2.hobbies) # [] 互不干扰
print(id(u1.hobbies))
print(id(u2.hobbies)) # id不一样，各自独立的列表


#=================================================================
#
# @dataclass
# class User:
#     name: str
#     # repr=False：打印实例时不显示该字段，适合敏感信息
#     password: str = field(repr=False)
#     # init=False：构造函数不接收该参数，需后续手动赋值
#     internal_id: str = field(init=False, default="")