import threading
import time

# 创建两把独立的互斥锁（死锁的前提：至少存在两把及以上锁）
lock_a = threading.Lock()
lock_b = threading.Lock()

def thread1_func():
    """线程1：先获取锁A，再尝试获取锁B"""
    print("线程1 启动，准备获取锁A...")
    # 1. 线程1成功获取锁A
    lock_a.acquire()
    print("线程1 已获取锁A，休眠1秒（确保线程2有时间获取锁B）...")
    time.sleep(1)  # 休眠让线程2有机会获取锁B，触发死锁条件

    # 2. 线程1尝试获取锁B（此时锁B已被线程2持有）
    print("线程1 准备获取锁B...")
    lock_b.acquire()  # 此处笔误，修正为 lock_b.acquire() —— 尝试获取锁B，会永久阻塞
    # 修正后的代码：
    # lock_b.acquire()
    print("线程1 已获取锁B，执行后续逻辑...")

    # 释放锁（若能执行到这里，不会死锁，实际永远执行不到）
    lock_b.release()
    lock_a.release()
    print("线程1 释放所有锁，执行完毕！")

def thread2_func():
    """线程2：先获取锁B，再尝试获取锁A"""
    print("线程2 启动，准备获取锁B...")
    # 1. 线程2成功获取锁B
    lock_b.acquire()
    print("线程2 已获取锁B，休眠1秒（确保线程1有时间获取锁A）...")
    time.sleep(1)  # 休眠让线程1有机会获取锁A，触发死锁条件

    # 2. 线程2尝试获取锁A（此时锁A已被线程1持有，开始阻塞）
    print("线程2 准备获取锁A...")
    lock_a.acquire()  # 永久阻塞在这里
    print("线程2 已获取锁A，执行后续逻辑...")

    # 释放锁（永远执行不到）
    lock_a.release()
    lock_b.release()
    print("线程2 释放所有锁，执行完毕！")

if __name__ == "__main__":
    # 创建两个线程
    t1 = threading.Thread(target=thread1_func, name="线程1")
    t2 = threading.Thread(target=thread2_func, name="线程2")

    # 启动线程
    t1.start()
    t2.start()

    # 等待线程执行（会永久阻塞在这里，程序无法退出）
    t1.join()
    t2.join()

    print("所有线程执行完毕！")  # 永远无法执行到这一行