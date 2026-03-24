import re

# 测试日志内容
log_content = """2024-01-15 10:30:01 [INFO] Test started: test_login
2024-01-15 10:30:02 [PASS] test_login completed in 1.2s
2024-01-15 10:30:03 [INFO] Test started: test_data_validation
2024-01-15 10:30:05 [FAIL] test_data_validation failed: Invalid email format
2024-01-15 10:30:06 [INFO] Test started: test_performance
2024-01-15 10:30:21 [PASS] test_performance completed in 15.0s"""

# 正则匹配  非捕获分组的内部（）正常能够捕获
pattern = r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} \[(PASS|FAIL)\] (\w+) (?:completed in (\d+\.\d+s)|failed: (.*))'
matches = re.findall(pattern, log_content)

print(matches)
# 1. 统计PASS/FAIL数量&百分比
total_tests = len(matches)
pass_count = sum(1 for res, _, _, _ in matches if res == "PASS")
fail_count = total_tests - pass_count
pass_rate = (pass_count / total_tests) * 100
fail_rate = (fail_count / total_tests) * 100

# 2. 计算平均执行时间（仅PASS用例有时间）
exec_times = [float(time[:-1]) for res, _, time, _ in matches if res == "PASS" and time]
avg_time = sum(exec_times) / len(exec_times) if exec_times else 0

# 3. 找出执行时间超10秒的测试
long_tests = [name for res, name, time, _ in matches if res == "PASS" and float(time[:-1]) > 10]

# 4. 失败测试的原因
fail_reasons = {name: reason for res, name, _, reason in matches if res == "FAIL"}