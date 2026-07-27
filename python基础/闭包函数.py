def outer(msg):
    text = msg
    def inner():
        print(text)
    return inner

f = outer("test")
# 查看闭包捕获的自由变量
print(f.__code__.co_freevars)  # ('text',)
# 查看保存自由变量值的单元格对象
print(f.__closure__)


# 自由变量：内部函数使用，但不在自身作用域定义的变量；
# Python 不会直接保存变量本身，而是存入 cell（单元格对象）；
# 闭包函数对象内部绑定了 cell，所以外部函数执行结束变量不会被回收。




# cell 保存的是「变量引用」，不是当时的值副本！
funcs = []
for i in range(3):
    def inner():
        print(i)
    funcs.append(inner)

funcs[0]()  # 2
funcs[1]()  # 2
funcs[2]()  # 2


#inner 捕获的是当前 make_func 作用域内的 val 变量引用，不是调用瞬间 i 的快照。

def make_func(val):
    def inner():
        print(val)
    val += 1   # 修改当前作用域的val
    return inner

funcs = []
for i in range(3):
    funcs.append(make_func(i))

funcs[0]() # 1
funcs[1]() # 2
funcs[2]() # 3

#这个也是闭包

funcs = []
for i in range(3):
    def inner():
        print(i)
    funcs.append(inner)
print(funcs[0].__code__.co_freevars)  # ('i',)
print(funcs[0].__closure__)           # 不为None，存在cell
funcs[0]() # 2
funcs[1]() # 2
funcs[2]() # 2inner是闭包吗？