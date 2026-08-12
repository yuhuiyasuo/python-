import socket
import time

# ===================== 配置项 =====================
CAMERA_IP = "169.254.50.50"
CAMERA_PORT = 2001
HANDSHAKE_REQ = "hello"  # 对应界面「交互请求文本」
HANDSHAKE_ACK = "world"  # 对应界面「交互回复文本」
TRIGGER_CMD = "start"  # 对应界面「触发文本」
CMD_ENDING = "\r\n"  # 指令结束符，若无效可依次换成 "\n" 或 ""
RECONNECT_DELAY = 3  # 重连间隔（秒）
RECV_TIMEOUT = 5  # 接收超时时间（秒）


# =================================================

def tcp_connect_and_handshake():
    """建立TCP连接并完成握手，成功返回socket对象，失败返回None"""
    client = None
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(RECV_TIMEOUT)
        print(f"[连接] 正在连接 {CAMERA_IP}:{CAMERA_PORT} ...")
        client.connect((CAMERA_IP, CAMERA_PORT))
        print("[连接] ✅ TCP连接建立成功")

        # 1. 强制完成握手，不握手相机不会响应后续指令
        handshake_msg = (HANDSHAKE_REQ + CMD_ENDING).encode("ascii")
        client.sendall(handshake_msg)
        print(f"[握手] 📤 已发送握手指令: {repr(handshake_msg)}")

        reply = client.recv(1024).decode("ascii", errors="ignore").strip()
        print(f"[握手] 📥 收到相机回复: {repr(reply)}")

        if reply == HANDSHAKE_ACK:
            print("[握手] ✅ 握手验证通过")
            return client
        else:
            print("[握手] ❌ 握手回复不匹配，相机拒绝后续指令")
            client.close()
            return None

    except Exception as e:
        print(f"[连接] ❌ 连接/握手失败: {e}")
        if client:
            try:
                client.close()
            except:
                pass
        return None


def continuous_scan():
    client_socket = None
    while True:
        # 连接断开时，重新建立连接+握手
        if client_socket is None:
            client_socket = tcp_connect_and_handshake()
            if client_socket is None:
                print(f"⏳ {RECONNECT_DELAY}秒后尝试重连...\n")
                time.sleep(RECONNECT_DELAY)
                continue

            # 握手成功后，发送持续触发指令
            try:
                trigger_msg = (TRIGGER_CMD + CMD_ENDING).encode("ascii")
                client_socket.sendall(trigger_msg)
                print(f"[触发] 📤 已发送持续触发指令: {repr(trigger_msg)}")
                print("[触发] ▶️  相机已进入持续扫码模式，等待条码...\n")
            except Exception as e:
                print(f"[触发] ❌ 发送触发指令失败: {e}")
                client_socket.close()
                client_socket = None
                continue

        # 循环接收扫码结果
        try:
            data = client_socket.recv(2048)
            # 空数据 = 连接已被相机主动断开
            if not data:
                print("[连接] ⚠️  相机主动断开了连接")
                client_socket.close()
                client_socket = None
                continue

            scan_result = data.decode("utf-8", errors="ignore").strip()
            if scan_result:
                print(f"[扫码] 📷 结果：{scan_result}")

        except socket.timeout:
            # 接收超时是正常的，说明暂无条码，继续等待
            continue
        except Exception as e:
            print(f"[接收] ❌ 异常：{e}")
            client_socket.close()
            client_socket = None
            print(f"⏳ {RECONNECT_DELAY}秒后自动重连...\n")
            time.sleep(RECONNECT_DELAY)


if __name__ == "__main__":
    try:
        continuous_scan()
    except KeyboardInterrupt:
        print("\n🚫 程序已手动停止")