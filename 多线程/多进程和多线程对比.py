import time
import threading
import multiprocessing

# I/O 密集型任务（模拟睡眠）
def io_task(duration):
    time.sleep(duration)

# CPU 密集型任务（模拟计算）
def cpu_task(n):
    count = 0
    for i in range(n):
        count += i

if __name__ == "__main__":
    # 测试参数
    num_tasks = 4
    io_duration = 2  # 秒
    cpu_iterations = 50000000

    # 1. 单线程 I/O
    start = time.time()
    for _ in range(num_tasks):
        io_task(io_duration)
    print(f"单线程 I/O: {time.time() - start:.2f}s")

    # 2. 多线程 I/O
    start = time.time()
    threads = [threading.Thread(target=io_task, args=(io_duration,)) for _ in range(num_tasks)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(f"多线程 I/O: {time.time() - start:.2f}s")  # 接近 2s（并行）

    # 3. 单线程 CPU
    start = time.time()
    for _ in range(num_tasks):
        cpu_task(cpu_iterations)
    print(f"单线程 CPU: {time.time() - start:.2f}s")

    # 4. 多线程 CPU（受 GIL 限制，无法并行）
    start = time.time()
    threads = [threading.Thread(target=cpu_task, args=(cpu_iterations,)) for _ in range(num_tasks)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(f"多线程 CPU: {time.time() - start:.2f}s")  # 接近单线程时间（GIL 限制）

    # 5. 多进程 CPU（真正并行）
    start = time.time()
    processes = [multiprocessing.Process(target=cpu_task, args=(cpu_iterations,)) for _ in range(num_tasks)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    print(f"多进程 CPU: {time.time() - start:.2f}s")  # 接近单线程时间 / CPU 核心数


