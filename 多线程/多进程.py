import time
import multiprocessing
from concurrent.futures import ProcessPoolExecutor  # 更现代的进程池写法


# ---------------------- 核心：模拟CPU密集型任务 ----------------------
def cpu_intensive_task(task_id: int, loop_count: int) -> None:
    """
    模拟CPU密集型任务（大量数值计算，无IO等待）
    :param task_id: 任务ID
    :param loop_count: 循环计算次数（越大越能体现CPU消耗）
    """
    print(f"[进程/任务{task_id}] 开始CPU密集计算（循环{loop_count}次）...")
    result = 0
    # 核心：纯CPU计算（无IO，不会释放GIL，多线程无效）
    for i in range(loop_count):
        result += i ** 2  # 平方计算，消耗CPU
    print(f"[进程/任务{task_id}] 计算完成！结果（前6位）：{str(result)[:6]}")


# ---------------------- 单进程执行 ----------------------
def run_single_process(tasks: list) -> float:
    """
    单进程逐个执行所有CPU密集型任务
    :param tasks: 任务列表，每个元素为 (task_id, loop_count)
    :return: 总耗时（秒）
    """
    start_time = time.time()
    # 单进程：串行执行所有任务
    for task in tasks:
        cpu_intensive_task(*task)
    total_time = time.time() - start_time
    return total_time


# ---------------------- 多进程执行（手动创建Process） ----------------------
def run_multi_process(tasks: list) -> float:
    """
    手动创建多进程执行任务（底层写法）
    :param tasks: 任务列表
    :return: 总耗时（秒）
    """
    start_time = time.time()
    processes = []

    # 1. 创建并启动所有子进程
    for task in tasks:
        # 创建子进程（target为任务函数，args为参数）
        p = multiprocessing.Process(target=cpu_intensive_task, args=task)
        processes.append(p)
        p.start()  # 启动进程（非阻塞，主进程继续执行）

    # 2. 等待所有子进程执行完成（阻塞主进程）
    for p in processes:
        p.join()  # 确保主进程等待子进程结束后再计算耗时

    total_time = time.time() - start_time
    return total_time


# ---------------------- 多进程执行（进程池，推荐） ----------------------
def run_multi_process_pool(tasks: list) -> float:
    """
    进程池执行任务（更简洁、高效，生产环境优先）
    :param tasks: 任务列表
    :return: 总耗时（秒）
    """
    start_time = time.time()
    # 创建进程池（max_workers建议设为CPU核心数，避免过度切换）
    cpu_core_num = multiprocessing.cpu_count()
    with ProcessPoolExecutor(max_workers=cpu_core_num) as executor:
        # 提交所有任务到进程池
        for task in tasks:
            executor.submit(cpu_intensive_task, *task)
    total_time = time.time() - start_time
    return total_time


# ---------------------- 主程序：对比测试 ----------------------
if __name__ == "__main__":
    # 重要：Windows系统下，多进程代码必须放在if __name__ == "__main__"内
    # 定义测试任务：4个任务，每个任务循环1亿次（CPU密集）
    test_tasks = [(1, 10000000), (2, 10000000), (3, 10000000), (4, 10000000)]

    # 1. 单进程执行
    print("=" * 60 + "\n【单进程执行】")
    single_time = run_single_process(test_tasks)

    # 2. 多进程（手动创建）执行
    print("\n" + "=" * 60 + "\n【多进程执行（手动创建Process）】")
    multi_process_time = run_multi_process(test_tasks)

    # 3. 多进程（进程池）执行（可选，效果与手动创建一致，更优雅）
    print("\n" + "=" * 60 + "\n【多进程执行（ProcessPoolExecutor）】")
    multi_pool_time = run_multi_process_pool(test_tasks)

    # ---------------------- 结果对比 ----------------------
    print("\n" + "=" * 60)
    print(f"CPU核心数：{multiprocessing.cpu_count()}")
    print(f"单进程总耗时：{single_time:.2f} 秒")
    print(f"多进程（手动）总耗时：{multi_process_time:.2f} 秒")
    print(f"多进程（进程池）总耗时：{multi_pool_time:.2f} 秒")
    print(f"多进程比单进程快：{single_time - multi_process_time:.2f} 秒")
    print("=" * 60)