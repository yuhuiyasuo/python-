import asyncio
import time


# 模拟IO密集型任务（如网络请求、数据库查询）
async def io_coroutine(task_id):
    print(f"协程{task_id}：开始IO等待...")
    # await 主动让出CPU，切换到其他协程执行
    await asyncio.sleep(1)  # 模拟IO等待（非阻塞）
    print(f"协程{task_id}：IO完成！")
    return f"任务{task_id}完成"


# 单线程串行执行（对比组）
def single_thread():
    start = time.time()
    for i in range(4):
        print(f"单线程任务{i}：开始IO等待...")
        #time.sleep(1)  # 阻塞式等待，总耗时≈8秒
        print(f"单线程任务{i}：IO完成！")
    print(f"单线程总耗时：{time.time() - start:.2f}秒")


# 协程执行（单线程内并发）
async def coroutine_main():
    start = time.time()
    # 创建4个协程任务
    tasks = [io_coroutine(i) for i in range(4)]
    # 并发执行所有协程
    results = await asyncio.gather(*tasks)
    print(f"协程总耗时：{time.time() - start:.2f}秒")  # 总耗时≈2秒
    print("结果：", results)


if __name__ == "__main__":
    print("===== 单线程串行 =====")
    single_thread()

    print("\n===== 协程并发 =====")
    asyncio.run(coroutine_main())  # 启动协程事件循环