def square_calculator_generator():
    """生成器：接收数字，产出其平方值；接收 quit，终止运行"""
    print("【生成器】已就绪，等待接收数字...")
    result = None
    while True:
        # 1. yield 产出上一次的处理结果，同时等待接收新数据
        # 第一次执行时，result 为 None，先产出 None，然后暂停等待 send()
        data = yield result

        # 2. 处理接收的数据
        if data == "quit":
            print("【生成器】接收到退出指令，终止运行")
            break
        try:
            num = float(data)
            result = num ** 2
            print(f"【生成器】处理：{num} → {result}")
        except (ValueError, TypeError):
            result = f"【生成器】错误：无效输入 '{data}'，请传入数字"
            print(result)

    # 生成器终止时，最终的 yield 不会执行，后续调用会抛出 StopIteration
    return "生成器已正常退出"


if __name__ == "__main__":
    # 1. 创建生成器对象
    calc_gen = square_calculator_generator()

    # 2. 激活生成器（获取第一个 yield 产出的 None，生成器暂停在 data = yield result）
    first_output = next(calc_gen)
    print(f"【调用方】首次获取生成器输出：{first_output}\n")

    # 3. 循环向生成器发送数据，获取处理结果（完整通信闭环）
    input_list = [5, 8.9, "12", "python", 3.1415, "quit"]
    for item in input_list:
        # send() 传递数据，同时接收生成器下一个 yield 产出的结果
        output = calc_gen.send(item)
        print(f"【调用方】接收生成器结果：{output}\n")

    # 4. 捕获生成器终止后的 StopIteration（包含 return 的返回值）
    try:
        calc_gen.send(10)
    except StopIteration as e:
        print(f"【调用方】捕获生成器终止信号：{e.value}")