def consumer_generator():
    """生成器（消费者）：接收任务数据，处理并返回结果"""
    print("消费者生成器已就绪，等待接收任务...")
    total_processed = 0
    while True:
        # 接收生产者传递的任务数据，产出累计处理数量
        task_data = yield total_processed

        # 处理退出指令
        if task_data == "stop":
            print(f"消费者终止，累计处理任务数：{total_processed}")
            break

        # 模拟任务处理
        total_processed += 1
        print(f"\n消费者处理任务：{task_data}")
        print(f"当前累计处理任务数：{total_processed}")
        # 处理结果可通过下一次 yield 产出（此处产出累计数）


if __name__ == "__main__":
    # 1. 创建消费者生成器（核心：生成器作为消费者）
    consumer = consumer_generator()

    # 2. 激活生成器
    next(consumer)

    # 3. 生产者：循环生成任务，通过 send() 传递给消费者（生成器）
    task_list = ["数据预处理-1", "接口调用-2", "结果存储-3", "数据预处理-4"]
    for task in task_list:
        # 发送任务数据，接收消费者返回的累计处理数
        processed_count = consumer.send(task)
        print(f"生产者收到反馈：已累计处理 {processed_count} 个任务")

    # 4. 发送停止指令，终止消费者
    consumer.send("stop")

    # 5. 关闭生成器（可选，释放资源）
    consumer.close()
    print("\n生产者：所有任务处理完毕，程序结束")