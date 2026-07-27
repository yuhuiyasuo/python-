payment_registry = {}

class PaymentMeta(type):
    def __new__(cls, name, bases, attrs):
        new_cls = super().__new__(cls, name, bases, attrs)
        # 跳过基类，只注册具体实现类
        if name != "BasePayment":
            pay_name = attrs.get("pay_name", name.lower())
            payment_registry[pay_name] = new_cls
        return new_cls

# 基类指定元类
class BasePayment(metaclass=PaymentMeta):
    def pay(self, amount):
        raise NotImplementedError

# 子类自动完成注册
class AliPay(BasePayment):
    pay_name = "alipay"
    def pay(self, amount):
        print(f"支付宝支付 {amount} 元")
