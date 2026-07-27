payment_registry = {}

# 定义注册装饰器
def register_payment(name: str):
    def wrapper(cls):
        payment_registry[name] = cls
        return cls
    return wrapper

# 加装饰器即自动注册
@register_payment("alipay")
class AliPay:
    def pay(self, amount):
        print(f"支付宝支付 {amount} 元")

@register_payment("wechat")
class WeChatPay:
    def pay(self, amount):
        print(f"微信支付 {amount} 元")
