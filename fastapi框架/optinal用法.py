from typing import Optional, Union

#用来表示 “值可以是指定类型，也可以是 None

# 以下两种写法完全等价
age: Optional[int]
age: int | None
age: Union[int, str]



from typing import Optional

def get_name() -> Optional[str]:
    """返回字符串或者 None"""
    return None

def get_name1() -> str | None:
    return None

name: Optional[str] = None
name = "张三"


def find_user(user_id: int) -> Optional[str]:
    """找到返回用户名(str)，找不到返回None"""
    if user_id == 1:
        return "admin"
    return None

res = find_user(2)
if res is not None:
    print(res.upper())
else:
    print("未找到用户")
