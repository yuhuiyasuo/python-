# 导入线程安全队列（注意是queue模块，小写q）
import queue
import threading
import time

# 1. 创建一个线程安全的队列（默认无限容量，先进先出）
msg_queue = queue.Queue()

# 2. 生产者函数：往队列里放数据
def producer():
    print("生产者线程启动，开始往队列存数字...")
    for i in range(1, 11):  # 生产1-10这10个数字
        msg_queue.put(i)  # 往队列中存入数据（线程安全）
        print(f"生产者存入：{i}")
        time.sleep(0.5)  # 模拟生产耗时，放慢速度
    print("生产者线程执行完毕！")

# 3. 消费者函数：从队列里取数据
def consumer():
    print("消费者线程启动，开始从队列取数字...")
    for _ in range(1, 11):  # 对应生产者的10个数据
        num = msg_queue.get()  # 从队列中取出数据（线程安全，队列空时会阻塞等待）
        print(f"消费者取出：{num}")
        time.sleep(1)  # 模拟消费耗时，比生产慢（体现队列缓冲作用）
    print("消费者线程执行完毕！")

if __name__ == "__main__":
    # 创建生产者和消费者线程
    t_pro = threading.Thread(target=producer)
    t_con = threading.Thread(target=consumer)

    # 启动线程
    t_pro.start()
    t_con.start()

    # 等待两个线程执行完毕
    t_pro.join()
    t_con.join()

    # 验证队列最终为空
    print(f"队列是否为空：{msg_queue.empty()}")