import functools

def decorator1(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Decorator 1 before")
        func()  # 第一次调用原函数
        func()  # 第二次调用原函数
        print("Decorator 1 after")
    return wrapper

def decorator2(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Decorator 2 before")
        func(*args, **kwargs)  # 这里的 func 是原 greet
        print("Decorator 2 after")
    return wrapper

@decorator1
@decorator2
def greet():
    print("Hello!")

greet()