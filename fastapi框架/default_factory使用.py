from pydantic import BaseModel

class BadDemo(BaseModel):
    # ❌错误：类定义的时候，就创建好这一个list对象
    my_list: list[int] = []


a = BadDemo()
b = BadDemo()

print(f"a.my_list id:{id(a.my_list)}")
print(f"b.my_list id:{id(b.my_list)}")
# !!! a、b 是完全不同实例，但底层是同一个列表对象
print(a.my_list is b.my_list) # True

a.my_list.append(100)
print(f"a.my_list={a.my_list}") # [100]
print(f"b.my_list={b.my_list}") # [100]  ！！b被意外修改，发生串扰

#======================================================
from pydantic import BaseModel, Field

class GoodDemo(BaseModel):
    # ✅每实例化一次，调用lambda生成全新list
    my_list: list[int] = Field(default_factory=lambda: [])


a = GoodDemo()
b = GoodDemo()

print(f"a.my_list id:{id(a.my_list)}")
print(f"b.my_list id:{id(b.my_list)}")
print(a.my_list is b.my_list) # False，两个完全不同对象

a.my_list.append(100)
print(f"a.my_list={a.my_list}") # [100]
print(f"b.my_list={b.my_list}") # []，互不干扰