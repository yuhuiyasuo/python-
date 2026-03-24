def foo():
    print("foo")
    boo()

#foo()     #报错，python是从上到下按照顺序执行的，

def boo():
    print("boo")


foo()   #  不会报错，