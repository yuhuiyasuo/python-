import time
from concurrent.futures import ThreadPoolExecutor

def simulate_io_task(task_id, wait_time=2):
    print(f"[{time.strftime('%H:%M:%S')}] 开始执行 I/O 任务 {task_id}")
    time.sleep(wait_time)
    print(f"[{time.strftime('%H:%M:%S')}] 完成 I/O 任务 {task_id}")
    return f"任务 {task_id} 结果"

if __name__ == "__main__":
    start_time = time.time()

    with ThreadPoolExecutor(max_workers=3) as executor:
        # 1. 提交单个任务，返回 Future 对象（代表异步任务的未来结果）
        future1 = executor.submit(simulate_io_task, 1, 1)  # 任务1，等待1秒
        future2 = executor.submit(simulate_io_task, 2, 3)  # 任务2，等待3秒
        future3 = executor.submit(simulate_io_task, 3, 2)  # 任务3，等待2秒

        # 2. 操作 Future 对象，获取任务结果
        print("\n===== 主动获取任务结果 =====")
        # result() 方法：阻塞直到任务完成，返回任务结果
        print(future1.result())
        print(future2.result())
        print(future3.result())

        # 额外：判断任务是否完成（done()）、是否被取消（cancel()，仅未执行的任务可取消）
        print(f"\n任务 1 是否完成：{future1.done()}")
        print(f"任务 2 是否可取消：{future2.cancel()}")  # 任务已执行，返回 False

    print(f"\n总耗时：{time.time() - start_time:.2f} 秒")