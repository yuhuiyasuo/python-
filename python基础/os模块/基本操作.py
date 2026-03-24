# 1. 获取所有环境变量（返回字典）
import os

env = os.environ
print("所有环境变量：", env)

# 2. 获取指定环境变量（如Python路径、系统临时目录）
python_path = os.getenv("PYTHONPATH")  # 推荐使用，不存在返回None
# 等价于 os.environ.get("PYTHONPATH")
print("Python路径：", python_path)

# 3. 设置环境变量（仅在当前Python进程生效，不修改系统全局）
os.environ["MY_CUSTOM_ENV"] = "test_value"
print("自定义环境变量：", os.getenv("MY_CUSTOM_ENV"))  # 输出: test_value