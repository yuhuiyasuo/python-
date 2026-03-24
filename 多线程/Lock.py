import threading

total = 0
count = 100000
# 创建互斥锁实例
lock = threading.Lock()


def add():
    global total
    for _ in range(count):
        # 方式1：手动加锁、释放锁（需注意异常场景下的锁释放）
        # lock.acquire()
        # try:
        #     total += 1
        # finally:
        #     lock.release()

        # 方式2：使用with语句（推荐，自动加锁、自动释放锁，无需处理异常）
        with lock:
            total += 1


def sub():
    global total
    for _ in range(count):
        with lock:
            total -= 1


t1 = threading.Thread(target=add)
t2 = threading.Thread(target=sub)

t1.start()
t2.start()
t1.join()
t2.join()

# 预期结果为0，实际结果稳定为0（数据安全）
print("最终total值：", total)