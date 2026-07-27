# 注册器：全局字典
payment_registry = {}

# 具体实现类
class AliPay:
    def pay(self, amount):
        print(f"支付宝支付 {amount} 元")

class WeChatPay:
    def pay(self, amount):
        print(f"微信支付 {amount} 元")

# 手动登记到注册器
payment_registry["alipay"] = AliPay
payment_registry["wechat"] = WeChatPay

# 使用注册器
def create_payment(pay_type: str):
    pay_cls = payment_registry.get(pay_type)
    if not pay_cls:
        raise ValueError(f"不支持的支付方式: {pay_type}")
    return pay_cls()

create_payment("alipay").pay(100)
