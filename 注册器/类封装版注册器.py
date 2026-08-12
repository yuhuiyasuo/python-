class Registry:
    def __init__(self, name: str = "default"):
        self.name = name
        self._storage = {}  # 内部存储容器

    def register(self, name: str):
        """注册装饰器"""
        def wrapper(obj):
            if name in self._storage:
                raise KeyError(f"名称 [{name}] 已在 {self.name} 注册器中存在")
            self._storage[name] = obj
            return obj
        return wrapper

    def get(self, name: str):
        """按名称获取注册对象"""
        obj = self._storage.get(name)
        if obj is None:
            raise KeyError(f"[{name}] 未在 {self.name} 注册器中注册")
        return obj

    def list_all(self):
        """列出所有注册项名称"""
        return list(self._storage.keys())

# 创建支付领域的注册器实例
payment_registry = Registry("payment")


@payment_registry.register("alipay")
class AliPay:
    def pay(self, amount):
        print(f"支付宝支付 {amount} 元")

print(payment_registry.list_all())

#等价于
# # 第一步：先执行 register("alipay")，得到 wrapper 函数
# wrapper_func = payment_registry.register("alipay")
#
# # 第二步：把 AliPay 类作为参数传入 wrapper_func
# AliPay = wrapper_func(AliPay)

@payment_registry.register("wechat")
class WeChatPay:
    def pay(self, amount):
        print(f"微信支付 {amount} 元")

# 调用
pay_cls = payment_registry.get("alipay")
pay_cls().pay(200)

print(payment_registry.list_all())  # ['alipay', 'wechat']
