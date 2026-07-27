import enum

# ---------- 1. 定义回调函数（模拟业务逻辑） ----------
def turn_on_light(instruction):
    print(f"✅ 执行开灯操作，指令ID: {instruction.name}")

def turn_off_light(instruction):
    print(f"✅ 执行关灯操作，指令ID: {instruction.name}")

def switch_mode(instruction, mode="night"):
    print(f"✅ 切换灯光模式为 {mode}，指令ID: {instruction.name}")


# ---------- 2. 定义枚举类（类似你的 SystemVariableEnum） ----------

# 整个过程发生在「定义 class 的时候」，不是运行时调用！
# 代码运行到 class LightCommand 结束这一行，三个枚举对象已经全部实例化完成



# 加载 class LightCommand
#  ├─ 遍历类内常量赋值行
#  │   └─ TURN_ON = (arg1, arg2, arg3)
#  │       └─ EnumMeta 拦截
#  │           └─ 调用 LightCommand(arg1, arg2, arg3)
#  │               └─ 执行你写的 __init__
#  │           └─ 生成实例 → 赋值给 LightCommand.TURN_ON
#  ├─ 注册所有成员
#  └─ 类定义结束，实例全部就绪
#
# 运行时：
# cmd = LightCommand.TURN_ON  # 只是获取早已创建好的对象
# cmd.execute()

class LightCommand(enum.Enum):
    # 每个成员用元组定义：(显示名称, 默认值, 触发函数)

    # 普通类只会简单赋值；Enum元类EnumMeta拦截了这一步：
    # 识别TURN_ON是枚举成员名称；等号右侧("开灯指令", 0, turn_on_light)是传给构造器的参数列表；
    # 自动调用LightCommand("开灯指令", 0, turn_on_light)创建实例。

    TURN_ON = ("开灯指令", 0, turn_on_light)
    TURN_OFF = ("关灯指令", 0, turn_off_light)
    SWITCH_MODE = ("切换模式", "auto", switch_mode)

    # 构造方法：将元组拆包存储为实例属性
    def __init__(self, label, default_value, trigger_func):
        self.label = label          # 显示名称
        self.default_value = default_value   # 默认值
        self._trigger_func = trigger_func    # 绑定的回调函数

    # 执行方法：调用绑定的回调
    def execute(self, *args, **kwargs):
        print(f"🔄 执行指令: {self.label} (默认值: {self.default_value})")
        return self._trigger_func(self, *args, **kwargs)


# ---------- 3. 遍历枚举成员并操作 ----------

# 对于每一个赋值，它会自动调用 __init__ 方法，将元组拆包赋值给 self.label、self.default_value 和 self._trigger_func。
print("=" * 40)
print("【遍历枚举成员】")
for item in LightCommand:
    print(f"成员: {item.name}, 标签: {item.label}, 默认值: {item.default_value}")

print("\n" + "=" * 40)
print("【调用每个指令的 execute 方法】")
for item in LightCommand:
    item.execute()  # 触发回调

print("\n" + "=" * 40)
print("【带参数执行（切换模式）】")
# 单独调用 SWITCH_MODE 并传入额外参数
LightCommand.SWITCH_MODE.execute(mode="daylight")