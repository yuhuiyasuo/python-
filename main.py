from freezegun import freeze_time
from datetime import datetime

# 1. 模拟时间演示
with freeze_time("2026-01-01 12:00:00"):
    print("模拟时间内:", datetime.now())

print("真实系统时间:", datetime.now())
print()

# 2. 正确的时间比较：字符串先转 datetime 对象
front_time = "2027-01-01 12:00:00"
print(type(front_time))
front_time = datetime.strptime(front_time, "%Y-%m-%d %H:%M:%S")
sys_time = datetime.now()

print("前端时间:", front_time)
print("系统时间:", sys_time)
print("前端时间 > 系统时间:", front_time > sys_time)  # 输出 True 或 False
