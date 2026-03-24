class SingletonMeta(type):
    # 缓存实例的字典
    _instances = {}

    def __call__(cls, *args, **kwargs):
        # __call__方法在类被实例化时调用（如Singleton()）
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


# 用自定义元类创建单例类
class Singleton(metaclass=SingletonMeta):
    def __init__(self, value):
        self.value = value


# 测试代码
if __name__ == "__main__":
    s1 = Singleton(100)
    s2 = Singleton(200)

    print(s1 is s2)  # 输出：True
    print(s1.value)  # 输出：100（仅初始化一次）