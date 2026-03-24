class A:
    def hello(self):
        print("Hello from A")
class B(A):
    def hello(self):
        super().hello()
        print("Hello from B")
class C(A):
    def hello(self):
        super().hello()
        print("Hello from C")
class D(B, C):
    def hello(self):
        super().hello()
        print("Hello from D")
d = D()
d.hello()
# 查看 D 的 MRO 顺序（关键！）
print(D.__mro__)

# 输出：(<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>) obj类自身对象
