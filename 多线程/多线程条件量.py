import threading
import time
from queue import Queue

# 1. 定义共享资源和条件量
MAX_QUEUE_SIZE = 5  # 队列最大容量
shared_queue = Queue(maxsize=MAX_QUEUE_SIZE)
cond = threading.Condition()  # 创建Condition对象，默认使用RLock


# 2. 定义生产者线程
def producer(producer_name):
    while True:
        # 必须先获取锁
        with cond:  # 用with语句自动管理acquire()和release()，更优雅
            # 循环判断条件：队列已满则等待（避免虚假唤醒，必须用while而非if）
            while shared_queue.full():
                print(f"【生产者{producer_name}】队列已满，等待消费者消费...")
                cond.wait()  # 释放锁，进入等待状态

            # 条件满足（队列未满），生产数据
            data = f"数据-{time.time():.2f}"
            shared_queue.put(data)
            print(f"【生产者{producer_name}】生产数据：{data}，当前队列长度：{shared_queue.qsize()}")

            # 通知消费者：队列非空，可消费（唤醒一个等待的消费者）
            cond.notify()

        # 模拟生产耗时（释放锁后执行，避免长时间占用锁）
        time.sleep(1)


# 3. 定义消费者线程
def consumer(consumer_name):
    while True:
        # 必须先获取锁
        with cond:
            # 循环判断条件：队列空则等待（避免虚假唤醒，必须用while而非if）
            while shared_queue.empty():
                print(f"【消费者{consumer_name}】队列空，等待生产者生产...")
                cond.wait()  # 释放锁，进入等待状态

            # 条件满足（队列非空），消费数据
            data = shared_queue.get()
            print(f"【消费者{consumer_name}】消费数据：{data}，当前队列长度：{shared_queue.qsize()}")

            # 通知生产者：队列未满，可生产（唤醒一个等待的生产者）
            cond.notify()

        # 模拟消费耗时（释放锁后执行，避免长时间占用锁）
        time.sleep(2)


# 4. 创建并启动线程
if __name__ == "__main__":
    # 创建2个生产者线程，3个消费者线程
    producers = [
        threading.Thread(target=producer, args=(f"P{i + 1}",))
        for i in range(2)
    ]
    consumers = [
        threading.Thread(target=consumer, args=(f"C{i + 1}",))
        for i in range(3)
    ]

    # 启动所有线程
    for p in producers:
        p.daemon = True  # 设为守护线程，主线程退出时子线程也退出
        p.start()
    for c in consumers:
        c.daemon = True
        c.start()

    # 主线程保持运行
    while True:
        time.sleep(10)