import threading
import time

# 创建Event实例
start_event = threading.Event()

def worker(name):
    """工作线程：等待开始指令，支持超时"""
    print(f"【工作线程】{name} 已就绪，等待开始指令...")
    # 等待指令，超时时间5秒（若5秒未收到指令，自动唤醒）
    wait_result = start_event.wait(timeout=5)
    if wait_result:
        # 收到指令（标志位为True）
        print(f"【工作线程】{name} 接收到开始指令，执行任务...")
        time.sleep(1)  # 模拟任务执行
        print(f"【工作线程】{name} 任务执行完毕！")
    else:
        # 超时未收到指令（标志位仍为False）
        print(f"【工作线程】{name} 等待指令超时（5秒），放弃执行任务！")

# 创建3个工作线程并启动
worker_threads = []
for i in range(3):
    t = threading.Thread(target=worker, args=(f"工作线程{i+1}",))
    worker_threads.append(t)
    t.start()

# 主线程：延迟2秒发送开始指令
time.sleep(2)
print(f"\n【主线程】发送开始执行指令！")
start_event.set()

# 等待第一批工作线程执行完毕
for t in worker_threads:
    t.join()

# 重置Event标志位，为后续线程做准备
print(f"\n【主线程】重置开始指令标志位！")
start_event.clear()
print(f"当前标志位状态：{start_event.is_set()}")  # 输出 False

# 再创建1个工作线程，验证标志位重置后的阻塞效果
t4 = threading.Thread(target=worker, args=("工作线程4",))
t4.start()
t4.join()