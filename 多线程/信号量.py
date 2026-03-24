import threading
import time

# 初始化信号量，允许同时2个线程获取
sem = threading.Semaphore(2)

def task(name):
    with sem:
        print(f"{name} 获取资源，开始执行")
        time.sleep(2)
        print(f"{name} 释放资源，执行完毕")

# 创建5个线程，同一时刻仅2个线程能执行
for i in range(5):
    t = threading.Thread(target=task, args=(f"线程{i}",))
    t.start()