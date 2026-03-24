import functools
import time

# 装饰器1：日志
def log_decorator(func):
    @functools.wraps(func)   #保留函数的元信息
    def wrapper(*args, **kwargs):
        print(args)
        print(f"[LOG] 函数 {func.__name__} 开始执行...")
        result = func(*args, **kwargs)
        print("result:")
        print(result)
        print(f"[LOG] 函数 {func.__name__} 执行结束！")
        return result

    return wrapper

# 装饰器2：计时
def time_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):  #wrapper实际指向的是calculate函数，所以能看到他的参数
        print(args)
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"[TIME] 函数 {func.__name__} 执行耗时：{end_time - start_time:.4f}s")
        return result
    return wrapper

# 叠加装饰器：先 @log_decorator，再 @time_decorator
@log_decorator
@time_decorator
def calculate(x):
    # 模拟耗时操作
    time.sleep(1)
    return x * 10

print(calculate(5))