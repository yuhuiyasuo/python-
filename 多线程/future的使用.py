"""
future_demo.py

演示 Future 的完整使用方法

运行：
    python future_demo.py
"""

import time
import threading
from concurrent.futures import ThreadPoolExecutor


def work(task_name, seconds):
    """模拟耗时任务"""

    print(f"[{threading.current_thread().name}] {task_name} 开始执行")

    for i in range(seconds):
        print(f"{task_name} 正在执行... {i + 1}/{seconds}")
        time.sleep(1)

    print(f"[{threading.current_thread().name}] {task_name} 执行结束")

    return f"{task_name} 执行成功"


def work_error():
    """模拟异常任务"""

    print(f"[{threading.current_thread().name}] work_error 开始")

    time.sleep(2)

    raise Exception("任务执行失败！")


#当 Future 对应的任务执行结束（无论成功还是失败），自动调用你指定的函数。
def callback(future):
    """Future完成后的回调"""

    print("\n========== 回调函数 ==========")

    if future.exception():
        print("任务异常：", future.exception())
    else:
        print("任务结果：", future.result())

    print("=============================\n")


def main():

    executor = ThreadPoolExecutor(max_workers=2)

    print("========== 提交正常任务 ==========")

    future1 = executor.submit(work, "Task-A", 5)

    print("Future对象：", future1)

    future1.add_done_callback(callback)

    print("\n========== 查询状态 ==========")

    while not future1.done():

        print("running :", future1.running())
        print("done    :", future1.done())
        print("--------------------")

        time.sleep(1)

    print("\n========== 获取结果 ==========")

    result = future1.result()

    print("返回值：", result)

    print("\n========== 提交异常任务 ==========")

    future2 = executor.submit(work_error)

    future2.add_done_callback(callback)

    try:
        future2.result()
    except Exception as e:
        print("捕获到异常：", e)

    print("\n========== Future最终状态 ==========")

    print("future1.done() =", future1.done())
    print("future2.done() =", future2.done())

    executor.shutdown()

    print("\n线程池关闭")


if __name__ == "__main__":
    main()