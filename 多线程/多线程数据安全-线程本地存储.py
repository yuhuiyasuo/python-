import threading
import time

# 创建线程本地对象
local_data = threading.local()

def worker():
    # 每个线程的local_data.count是独立副本
    local_data.count = 0
    for _ in range(100000):
        local_data.count += 1
    # 打印当前线程的计数（互不干扰）
    print(f"线程 {threading.current_thread().name} 计数：{local_data.count}")

t1 = threading.Thread(target=worker, name="t1")
t2 = threading.Thread(target=worker, name="t2")
t1.start()
t2.start()
t1.join()
t2.join()