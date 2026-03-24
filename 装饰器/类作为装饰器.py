import time

# 类的__init__方法接收被装饰的对象（函数 / 类）作为参数，用于保存被装饰对象的引用；
# 类实现__call__方法，该方法作为装饰后的逻辑入口，负责包装被装饰对象的执行过程（如添加前置 / 后置操作、修改参数 / 返回值等）。
class TimerDecorator:
    def __init__(self, func):
        # __init__接收被装饰的函数
        self.func = func  # 保存被装饰函数的引用

    def __call__(self, *args, **kwargs):
        # __call__实现装饰逻辑，*args/**kwargs适配任意参数的函数
        start = time.time()
        result = self.func(*args, **kwargs)  # 执行原函数
        end = time.time()
        print(f"函数{self.func.__name__}执行时间：{end - start:.6f}秒")
        return result  # 返回原函数的执行结果


# 使用类装饰器装饰函数
@TimerDecorator
def calculate_sum(n):
    return sum(range(n))


# 调用装饰后的函数
calculate_sum(1000000)