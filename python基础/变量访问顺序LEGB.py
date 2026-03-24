# Built-in：内置的min函数
# Global：全局变量x=1

#LEGB 是 Python 中变量查找的核心规则，全称是 Local → Enclosing → Global → Built-in（局部→嵌套→全局→内置）
x = 1

def outer():
    # Enclosing：外层变量x=2
    x = 2
    def inner():
        # Local：局部变量x=3（优先级最高）
        x = 3
        print(x)  # Local → 3
        print(min(x, 0))  # 局部无min → 找内置min → 0
    inner()

outer()

# 去掉inner的局部x
def outer2():
    x = 2
    def inner2():
        print(x)  # 局部无x → Enclosing → 2
    inner2()

outer2()

# 去掉outer2的x
def outer3():
    def inner3():
        print(x)  # 局部/Enclosing无x → Global → 1
    inner3()

outer3()