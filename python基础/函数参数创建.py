print("before")

def foo(x=[]):
    return x

print("after")


# before
#
# ↓
#
# 创建 []
#
# ↓
#
# 保存到 foo.__defaults__
#
# ↓
#
# after