import threading
import time

# 用于通知线程停止的 Event
stop_event = threading.Event()

def worker():
    print("线程启动，开始循环执行任务...")
    # 循环执行，直到收到“停止信号”
    while not stop_event.is_set():
        print("执行单次任务...")
        time.sleep(1)
    print("收到停止信号，线程退出")

t = threading.Thread(target=worker)
t.start()

# 主线程：5秒后发送“停止信号”
time.sleep(5)
print("主线程：发送停止信号！")
stop_event.set()

t.join()
print("主线程结束")