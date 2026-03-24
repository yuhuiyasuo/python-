#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
继承与多态完整演示示例
涵盖：单继承、多继承（MRO）、方法重写、super()、多态调用、鸭子类型
"""

# ===================== 第一部分：单继承基础 =====================
# 父类：定义通用属性和方法
class Animal:
    """动物基类"""
    def __init__(self, name, age):
        # 通用属性：名字、年龄
        self.name = name
        self.age = age

    def basic_info(self):
        """通用方法：打印基础信息"""
        return f"【{self.name}】 年龄：{self.age}岁"

    def speak(self):
        """父类通用方法（子类将重写）"""
        print("父类的speak方法")
        #raise NotImplementedError("子类必须实现speak方法")

    def eat(self):
        """父类通用方法（子类可复用或重写）"""
        print(f"{self.name} 正在吃通用食物～")


# 子类1：猫（单继承Animal）
class Cat(Animal):
    """猫类，继承自动物类"""
    def __init__(self, name, age, hair_color):
        # 调用父类初始化方法，复用属性定义
        super().__init__(name, age)
        # 子类扩展专属属性：毛色
        self.hair_color = hair_color

    # 重写父类speak方法（多态基础）
    def speak(self):
        return f"{self.name}（{self.hair_color}毛）：喵喵喵～"

    # 重写父类eat方法，定制化逻辑
    def eat(self):
        print(f"{self.name} 正在吃小鱼干～")


# 子类2：狗（单继承Animal）
class Dog(Animal):
    """狗类，继承自动物类"""
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        # 子类扩展专属属性：品种
        self.breed = breed

    # 重写父类speak方法（多态基础）
    def speak(self):
        super(Dog,self).speak()    #调用父类的方法
        #return f"{self.name}（{self.breed}）：汪汪汪～"

    # 子类新增专属方法
    def guard_house(self):
        print(f"{self.name} 正在看家护院～")


# ===================== 第二部分：多继承演示（MRO规则） =====================
class Flyable:
    """可飞行的混合类（多继承用）"""
    def fly(self):
        return f"{self.name} 正在空中飞行～"

    # 与Animal同名方法，演示MRO查找顺序
    def eat(self):
        print(f"{self.name} 正在吃飞行专属食物（虫子）～")


# 多继承：同时继承Animal和Flyable
class Bird(Animal, Flyable):
    """鸟类，继承自动物类+可飞行类"""
    def __init__(self, name, age, wing_length):
        super().__init__(name, age)
        self.wing_length = wing_length  # 专属属性：翼长

    def speak(self):
        return f"{self.name}（翼长{self.wing_length}cm）：叽叽喳喳～"


# ===================== 第三部分：多态核心调用 =====================
def animal_interact(animal):
    """
    多态核心函数：统一接口，适配所有Animal子类
    无需判断具体类型，只要有对应方法即可调用
    """
    print("\n" + "-"*50)
    print(animal.basic_info())       # 调用通用方法
    print(animal.speak())            # 调用重写后的方法（多态体现）
    animal.eat()                     # 调用可能重写的方法

    # 可选：调用子类专属方法（演示类型判断）
    if hasattr(animal, "guard_house"):
        animal.guard_house()
    if hasattr(animal, "fly"):
        print(animal.fly())



# ===================== 主程序运行测试 =====================
if __name__ == "__main__":
    print("===== 1. 单继承演示（猫/狗） =====")
    # 创建猫对象
    cat = Cat(name="小白", age=2, hair_color="纯白")
    animal_interact(cat)

    # 创建狗对象
    dog = Dog(name="大黄", age=3, breed="金毛")
    animal_interact(dog)

    # print("\n===== 2. 多继承演示（鸟类） =====")
    # # 打印Bird类的MRO（方法解析顺序）
    # print("Bird类的MRO顺序：", Bird.__mro__)
    # bird = Bird(name="小燕", age=1, wing_length=15)
    # animal_interact(bird)  # 自动调用Animal/Flyable的方法（按MRO）
    #
    # print("\n===== 3. 鸭子类型演示（非Animal子类） =====")
    # robot_dog = RobotDog(name="旺财一号", age=1)
    # animal_interact(robot_dog)  # 无继承但可调用，体现Python动态多态
    #
    # print("\n===== 4. super()与父类方法调用细节 =====")
    # # 演示子类中调用父类未重写的方法
    # temp_cat = Cat("小黑", 1, "纯黑")
    # # 手动调用父类的eat方法（跳过子类重写）
    # super(Cat, temp_cat).eat()