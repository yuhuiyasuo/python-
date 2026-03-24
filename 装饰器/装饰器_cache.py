import functools


def cache(func):
    # 用字典缓存函数结果（key：参数，value：返回值）
    cache_dict = {}

    @functools.wraps(func)   #保留原函数的元信息
    def wrapper(*args):
        if args in cache_dict:
            print(f"缓存命中：{func.__name__}{args}")
            return cache_dict[args]
        # 未命中缓存，执行函数并缓存结果
        result = func(*args)
        cache_dict[args] = result
        print(f"缓存未命中：{func.__name__}{args}")
        return result

    return wrapper


@cache
def factorial(n):
    # 计算阶乘（递归）
    return 1 if n <= 1 else n * factorial(n - 1)


factorial(5)
factorial(5)  # 第二次调用命中缓存