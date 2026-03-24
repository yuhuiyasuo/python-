import threading

# 创建可重入锁
rlock = threading.RLock()
shared_data = "初始数据"

def inner_func():
    """嵌套函数：需要获取同一把锁"""
    with rlock:
        global shared_data
        shared_data += " - 内部函数修改"
        print(f"内部函数执行，共享数据：{shared_data}")

def outer_func(thread_id):
    """外部函数：获取锁并调用嵌套函数"""
    with rlock:
        global shared_data
        shared_data = f"线程 {thread_id} - 外部函数初始化"
        print(f"外部函数执行，共享数据：{shared_data}")
        # 调用嵌套函数，再次获取同一把 rlock（可重入，无死锁）
        inner_func()

if __name__ == "__main__":
    t1 = threading.Thread(target=outer_func, args=(1,))
    t2 = threading.Thread(target=outer_func, args=(2,))

    t1.start()
    t2.start()
    t1.join()
    t2.join()