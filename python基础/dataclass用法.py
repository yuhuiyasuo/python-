from dataclasses import dataclass

@dataclass
class Student:
    name: str
    age: int

# 等价于
# class Student:
#     def __init__(self, name: str, age: int):
#         self.name = name
#         self.age = age
#
#     def __repr__(self):
#         return f"Student(name={self.name}, age={self.age})"
#
#     def __eq__(self, other):
#         return (
#             self.name == other.name
#             and self.age == other.age
#         )

s = Student("Tom", 18)

print(s)


from dataclasses import dataclass, field

@dataclass
class Student:
    scores: list = field(default_factory=list)   #list是一个函数，后续是调用


# @dataclass
# class Student1:
#     scores: list = field(default=[])   #在类创建的时候【】就存在，后续共享