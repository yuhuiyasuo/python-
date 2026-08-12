import socket
import time

def send_trigger(host, trigger_port=2001, trigger_cmd=b"START\r\n"):
    """向读码器触发端口发送启动指令"""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(5)
            sock.connect((host, trigger_port))
            sock.send(trigger_cmd)
            print(f"已向 {host}:{trigger_port} 发送触发指令")
            return True
    except Exception as e:
        print(f"触发失败: {e}")
        return False

def read_code(host, port, timeout=30):
    """连接读码器数据端口，等待并读取条码内容"""
    data = bytearray()
    deadline = time.time() + float(timeout)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(1)
        sock.connect((host, int(port)))
        print(f"已连接到数据端口 {host}:{port}")

        while time.time() < deadline:
            try:
                chunk = sock.recv(1024)
            except socket.timeout:
                if data:
                    # 已有部分数据，继续等待结束符
                    continue
                else:
                    continue

            if not chunk:
                break

            data.extend(chunk)

            # 海康输出格式以分号、回车或换行结束
            if b";" in data or b"\r" in data or b"\n" in data:
                break

    code = data.decode("utf-8", errors="ignore").strip()
    code = code.strip(";\r\n ")
    print(f"收到扫码结果: {code}")
    return code

def start_main(params_dict):
    """
    主控函数，参数顺序（按原变量列表）：
        variables[0] -> IP地址
        variables[1] -> 数据端口（如9003）
        variables[2] -> 发送数据（旧配置，现忽略）
        variables[3] -> 变量ID（用于写入结果）
        variables[5] -> 超时时间（可选）
    """
    variables = params_dict.get("variables", [])
    if len(variables) < 4:
        raise ValueError("参数不足，需要至少 IP、端口、发送数据占位、变量ID")

    ip = variables[0]["value"]
    data_port = int(variables[1]["value"])
    variable_id = variables[3]["value"]
    timeout = int(variables[5]["value"]) if len(variables) > 5 else 30

    # ---- 循环重试配置 ----
    MAX_RETRIES = 30          # 最大重试次数，可根据需要调整
    RETRY_DELAY = 0.5         # 重试前等待时间（秒）
    TRIGGER_PORT = 2001
    TRIGGER_CMD = b"START\r\n"

    retry_count = 0
    code = None

    while retry_count < MAX_RETRIES:
        retry_count += 1
        print(f"\n===== 第 {retry_count} 次尝试 =====")

        # ---- 1. 触发扫码 ----
        if not send_trigger(ip, TRIGGER_PORT, TRIGGER_CMD):
            print("触发失败，等待后重试...")
            time.sleep(RETRY_DELAY)
            continue

        # 等待设备响应（可适当延时）
        time.sleep(0.5)

        # ---- 2. 读取扫码结果 ----
        try:
            code = read_code(ip, data_port, timeout)
        except Exception as e:
            print(f"读取过程发生异常: {e}，将重试...")
            time.sleep(RETRY_DELAY)
            continue

        # ---- 3. 判断是否成功 ----
        if code:
            print(f"扫码成功！结果: {code}")
            break
        else:
            print("未收到有效扫码结果，准备重试...")
            time.sleep(RETRY_DELAY)
            continue

    # 若循环结束仍未成功
    if not code:
        raise TimeoutError(f"超过最大重试次数 ({MAX_RETRIES})，扫码失败")

    # ---- 4. 写入变量 ----
    # variable_write_throw_exception(variable_id, code)
    print(f"扫码结果已写入变量 {variable_id}")

    return params_dict


if __name__ == "__main__":
    # 测试示例
    HOST = "169.254.50.50"
    DATA_PORT = 9003
    test_params = {
        "variables": [
            {"value": HOST},
            {"value": DATA_PORT},
            {"value": ""},          # 占位
            {"value": "target_var"} # variable_id
        ]
    }
    start_main(test_params)