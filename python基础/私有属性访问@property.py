class Parent:
    def __init__(self):
        # 定义父类私有属性（双下划线开头，名称改写生效）
        self.__private_attr = "父类私有属性初始值"

    # 用 @property 装饰器封装私有属性的获取接口（getter）
    # 方法名（private_attr）就是暴露给外部/子类的「属性名」
    @property
    def private_attr(self):
        """获取父类私有属性，通过 @property 伪装成属性访问"""
        # 可在此处添加额外逻辑（如日志、数据处理等）
        print("正在获取父类私有属性...")
        return self.__private_attr

    # 可选：用 @属性名.setter 装饰器封装私有属性的修改接口（setter）
    # 方法名必须和 @property 装饰的方法名一致（private_attr）
    @private_attr.setter
    def private_attr(self, new_value):
        """修改父类私有属性，附带参数合法性校验"""
        # 自定义校验逻辑，保证属性值合法
        if isinstance(new_value, str) and len(new_value) > 0:
            print("正在修改父类私有属性...")
            self.__private_attr = new_value
        else:
            raise ValueError("私有属性值必须是非空字符串")


# 子类继承父类
class Child(Parent):
    def __init__(self):
        # 调用父类构造方法，初始化父类私有属性
        super().__init__()

    # 子类中访问/修改父类通过 @property 封装的私有属性
    def operate_parent_private(self):
        # 1. 访问父类私有属性（语法：self.属性名，无需加括号，如同访问普通属性）
        current_value = self.private_attr
        print(f"子类访问到父类私有属性：{current_value}")

        # 2. 修改父类私有属性（语法：self.属性名 = 新值，触发 @private_attr.setter 方法）
        self.private_attr = "子类通过 @property 修改后的属性值"

        # 3. 再次访问，验证修改结果
        updated_value = self.private_attr
        print(f"子类修改后，父类私有属性：{updated_value}")


# 测试代码
if __name__ == "__main__":
    child = Child()
    child.operate_parent_private()