class Parent:
    def __init__(self, score):
        self._score = score

    @property
    def score(self):
        print("父类 score getter：获取原始分数")
        return self._score

    @score.setter
    def score(self, value):
        print("父类 score setter：验证分数有效性")
        if not (0 <= value <= 100):
            raise ValueError("分数必须在0-100之间")
        self._score = value

class Child(Parent):
    @property
    def score(self):
        # 调用父类的 score getter，保留父类逻辑
        parent_score = super().score
        # 子类扩展逻辑：添加分数等级描述
        if parent_score >= 90:
            level = "优秀"
        elif parent_score >= 60:
            level = "及格"
        else:
            level = "不及格"
        return f"{parent_score}分（{level}）"

    # 子类重写 score setter，保留父类验证逻辑 + 扩展自身逻辑
    @score.setter
    def score(self, value):
        # 调用父类的 score setter，先执行父类的有效性验证
        super(Child, type(self)).score.__set__(self, value)
        # 子类扩展逻辑：打印分数修改日志
        print(f"子类扩展：分数已更新为 {self._score}")

# 测试
child = Child(85)
# 访问 score：触发子类 getter + 父类 getter
print(child.score)
# 修改 score：触发子类 setter + 父类 setter
child.score = 95
print(child.score)
# 测试无效分数（父类 setter 会抛出异常）
try:
    child.score = 105
except ValueError as e:
    print(e)