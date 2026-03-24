def singleton_decorator(cls):
    # 用字典缓存实例（支持多个类的单例）
    instances = {}

    def wrapper(*args, **kwargs):
        # 如果类不在缓存中，创建实例并缓存
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        # 返回缓存的实例
        return instances[cls]

    return wrapper


# 使用装饰器装饰类
@singleton_decorator
class MySingleton:
    def __init__(self, value):
        self.value = value


# 测试代码
if __name__ == "__main__":
    m1 = MySingleton(10)
    m2 = MySingleton(20)

    print(m1 is m2)  # 输出：True
    print(m1.value)  # 输出：10（装饰器方式不会覆盖初始化参数，因为只创建一次实例）