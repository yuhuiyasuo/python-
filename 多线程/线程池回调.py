import time
from concurrent.futures import ThreadPoolExecutor

def simulate_io_task(task_id, wait_time=2):
    print(f"[{time.strftime('%H:%M:%S')}] 开始执行 I/O 任务 {task_id}")
    time.sleep(wait_time)
    print(f"[{time.strftime('%H:%M:%S')}] 完成 I/O 任务 {task_id}")
    return {
        "task_id": task_id,
        "status": "success",
        "wait_time": wait_time
    }

def task_callback(future):
    """任务完成后的回调函数（参数必须是 Future 对象）"""
    # 从 Future 对象中获取任务结果
    result = future.result()
    print(f"\n[{time.strftime('%H:%M:%S')}] 回调函数处理结果：")
    print(f"  任务 {result['task_id']} - 状态：{result['status']}，等待时间：{result['wait_time']} 秒")

if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=2) as executor:
        # 提交任务并绑定回调函数
        future1 = executor.submit(simulate_io_task, 1, 2)
        future1.add_done_callback(task_callback)  # 绑定回调   线程完成之后会立即执行

        future2 = executor.submit(simulate_io_task, 2, 1)
        future2.add_done_callback(task_callback)  # 绑定回调

    # 无需手动获取结果，回调函数会自动触发
    print("\n所有任务提交完成，等待回调执行...")