# 类属性是在类定义时创建一次"这一机制。

class Student:
    nums = []


a = Student()
b = Student()


a.nums.append(1)


print(b.nums)