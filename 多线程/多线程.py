import time
import threading
from concurrent.futures import ThreadPoolExecutor  # 可选：更简洁的线程池写法


# ---------------------- 核心：模拟IO密集型任务 ----------------------
def io_task(task_id: int, sleep_time: float) -> None:
    """
    模拟IO密集型任务（如网络请求、文件读写）
    :param task_id: 任务ID
    :param sleep_time: 模拟IO等待时间（秒）
    """
    print(f"[任务{task_id}] 开始执行，等待{sleep_time}秒...")
    time.sleep(sleep_time)  # 核心：IO等待（释放GIL，其他线程可执行）
    print(f"[任务{task_id}] 执行完成！")


# ---------------------- 单线程执行 ----------------------
def run_single_thread(tasks: list) -> float:
    """
    单线程执行所有任务
    :param tasks: 任务列表，每个元素为 (task_id, sleep_time)
    :return: 总耗时（秒）
    """
    start_time = time.time()
    # 单线程：逐个执行任务
    for task in tasks:
        io_task(*task)
    total_time = time.time() - start_time
    return total_time


# ---------------------- 多线程执行（手动创建线程） ----------------------
def run_multi_thread(tasks: list) -> float:
    """
    多线程执行所有任务（手动创建线程）
    :param tasks: 任务列表
    :return: 总耗时（秒）
    """
    start_time = time.time()
    threads = []

    # 1. 创建并启动所有线程
    for task in tasks:
        t = threading.Thread(target=io_task, args=task)
        threads.append(t)
        t.start()  # 启动线程（非阻塞，主线程继续执行）

    # 2. 等待所有线程执行完成（阻塞主线程）
    for t in threads:
        t.join()

    total_time = time.time() - start_time
    return total_time


# ---------------------- 多线程执行（线程池，更简洁） ----------------------
def run_multi_thread_pool(tasks: list) -> float:
    """
    多线程执行（线程池写法，推荐生产环境使用）
    :param tasks: 任务列表
    :return: 总耗时（秒）
    """
    start_time = time.time()
    # 创建线程池（最大线程数建议不超过CPU核心数*5，IO密集型可适当增大）
    with ThreadPoolExecutor(max_workers=len(tasks)) as executor:
        # 提交所有任务到线程池
        for task in tasks:
            executor.submit(io_task, *task)
    total_time = time.time() - start_time
    return total_time


# ---------------------- 主程序：对比测试 ----------------------
if __name__ == "__main__":
    # 定义测试任务：4个任务，每个任务等待2秒
    test_tasks = [(1, 2), (2, 2), (3, 2), (4, 2)]

    print("=" * 50 + "\n【单线程执行】")
    single_time = run_single_thread(test_tasks)

    print("\n" + "=" * 50 + "\n【多线程执行（手动创建）】")
    multi_time = run_multi_thread(test_tasks)

    # 可选：测试线程池写法
    # print("\n" + "="*50 + "\n【多线程执行（线程池）】")
    # multi_pool_time = run_multi_thread_pool(test_tasks)

    # ---------------------- 结果对比 ----------------------
    print("\n" + "=" * 50)
    print(f"单线程总耗时：{single_time:.2f} 秒")
    print(f"多线程总耗时：{multi_time:.2f} 秒")
    # print(f"线程池总耗时：{multi_pool_time:.2f} 秒")
    print(f"多线程比单线程快：{single_time - multi_time:.2f} 秒")
    print("=" * 50)