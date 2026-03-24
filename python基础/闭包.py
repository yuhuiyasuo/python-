
#闭包是记住外层函数的变量的状态

'''
outer 执行完毕后，它的局部作用域本应被 Python 垃圾回收机制销毁（普通函数执行完，局部变量会被释放），但因为：
inner 函数引用了 outer 的局部变量 count（count 成为闭包的自由变量）；
inner 被返回并赋值给了全局变量 counter（存在 “活跃的引用”）；
Python 会将 count 打包到 inner 的 __closure__ 属性中（以 cell 对象的形式），因此 count 不会被销毁，而是被闭包保留下来。
'''
def outer(count):  # 外层函数，参数是局部变量
    # 内层函数：引用外层的count，且不立即执行
    def inner():
        nonlocal count  # 声明修改外层的不可变变量（int/str/tuple需加nonlocal） gloabl不可以，gloabl是修改全局变量
        count += 1
        return count

    return inner  # 返回内层函数的引用（无括号）


# 调用外层函数，得到内层函数的引用（闭包实例）
counter = outer(0)

# 多次调用闭包，持续修改外层的count
print(counter())  # 1
print(counter())  # 2
print(counter())  # 3

print("=============================")
a = []
for i in range(3):
    def fun(a):
        return i + a
    a.append(fun)
for f in a:
    print(f(1))    # 3 3 3

print("=============================")
a = []
for i in range(3):
    # 中间函数wrapper：接收当前循环的i，返回绑定后的fun
    def wrapper(i_val):
        def fun(a):
            return i_val + a  # 引用wrapper作用域的i_val（独立于外层i）
        return fun
    # 每次循环调用wrapper，传入当前i，得到绑定后的fun
    a.append(wrapper(i))
for f in a:
    print(f(1))  # 输出：1 2 3

print("=============================")

def outer():
    lst = [1, 2, 3]  # 外部变量：可变类型列表
    def inner():
        return lst
    return inner

closure = outer()
print(closure())  # [1,2,3]
# 外部修改可变类型变量，闭包读取的结果也会变化
lst_ref = closure()
lst_ref.append(4)
print(closure())  # [1,2,3,4]