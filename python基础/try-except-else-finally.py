#--------多个异常多个分支进行捕获

try:
    with open("data.txt", "r") as f:  # 可能抛FileNotFoundError/PermissionError
        content = f.read()
        num = int(content)  # 可能抛ValueError
# 分支1：处理“文件不存在”
except FileNotFoundError as e:
    print(f"错误：文件不存在 → {e}")
    print("请检查文件路径是否正确！")
# 分支2：处理“权限不足”
except PermissionError as e:
    print(f"错误：权限不足 → {e}")
    print("请修改文件读写权限！")
# 分支3：处理“内容非数字”
except ValueError as e:
    print(f"错误：文件内容不是数字 → {e}")
    print("请确保文件内只有数字！")





def test_finally_return():
    try:
        print("执行try块：计算10/0")
        10 / 0
        return "try的返回值"
    except ZeroDivisionError:
        return "except的返回值"
    finally:
        print("执行finally块：带return")
        return "finally的返回值"  # 覆盖之前的return

res = test_finally_return()
print(f"最终返回值：{res}")

# 输出：
# 执行try块：计算10/0
# 执行finally块：带return
# 最终返回值：finally的返回值

#一个except可以捕获多个异常情况
try:
    num = int(input("输入数字："))  # 可能抛ValueError
    result = 10 / num  # 可能抛ZeroDivisionError
except (ValueError, ZeroDivisionError) as e:
    # 无论触发哪种异常，都执行这段逻辑
    print(f"输入错误：{e}")  # e是异常对象，可获取错误详情
    print("请输入非0的有效数字！")







#--------------except Exception as e:通用异常
try:
    # 可能触发多种未知异常
    data = eval(input("输入一个Python表达式："))  # 语法错误、名称错误等
except SyntaxError as e:
    print(f"语法错误：{e}")
except NameError as e:
    print(f"名称错误：{e}")
# 兜底：处理其他所有未预判的异常
except Exception as e:
    print(f"未知错误：{type(e).__name__} → {e}")  # 打印异常类型+详情
    # 可选：记录日志、触发告警等