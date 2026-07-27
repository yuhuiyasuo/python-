class MyFile:
    """自定义文件上下文管理器：模拟自动关闭文件"""

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None  # 初始化文件句柄

    # 进入with块：打开文件，返回文件对象
    def __enter__(self):
        print("执行__enter__：打开文件")
        self.file = open(self.filename, self.mode)
        return self.file  # 赋值给as后的变量

    # 退出with块：关闭文件，处理异常
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("执行__exit__：关闭文件")
        if self.file:
            self.file.close()

        # 打印异常信息（如果有）
        if exc_type:
            print(f"捕获异常：{exc_type}, {exc_val}")
        # 返回False：不抑制异常（让异常正常抛出）
        return False


# 使用自定义上下文管理器
try:
    with MyFile("test.txt", "r") as f:
        print(f.read())
        # 故意触发异常（测试__exit__仍执行）
        1 / 0
except ZeroDivisionError:
    print("外部捕获到除零异常")


# 输出顺序：
# 执行__enter__：打开文件
# （文件内容）
# 执行__exit__：关闭文件
# 捕获异常：<class 'ZeroDivisionError'>, division by zero
# 外部捕获到除零异常