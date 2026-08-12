import binascii
import struct

# ---------- 模拟响应生成器 ----------
def build_mock_response(request_bytes):
    """
    根据 Modbus 读请求生成模拟响应报文（字节流）
    请求格式：01 03 起始地址(2B) 寄存器数量(2B) CRC(2B)
    响应格式：01 03 字节数 数据... CRC
    """
    # 解析请求
    addr, func, start_addr, num_regs = struct.unpack('>BBHH', request_bytes[:6])
    if func != 0x03 or num_regs != 3:
        raise ValueError("仅支持读取3个寄存器的请求")

    # 模拟测量数据（可自定义）
    mock_values = {
        0: 200,   # 最高点 (H)
        1: 50,    # 最低点 (L)
        2: 151    # 遮挡总数
    }

    # 构造数据部分（每个寄存器2字节，大端）
    data_bytes = b''
    for reg_addr in range(start_addr, start_addr + num_regs):
        val = mock_values.get(reg_addr, 0)
        data_bytes += struct.pack('>H', val)

    # 构造响应帧
    response = struct.pack('>BB', addr, func) + struct.pack('>B', len(data_bytes)) + data_bytes
    # 计算 CRC16 (Modbus)
    crc = crc16_modbus(response)
    response += struct.pack('<H', crc)   # 低字节在前
    return response

def crc16_modbus(data):
    """Modbus CRC16 计算"""
    crc = 0xFFFF
    for byte in data:
        crc ^= byte
        for _ in range(8):
            if crc & 0x0001:
                crc = (crc >> 1) ^ 0xA001
            else:
                crc >>= 1
    return crc

# ---------- 响应解析器 ----------
def parse_modbus_response(response_bytes):
    """
    解析 Modbus 响应，返回结构化数据
    符合您代码中的明治传感器 BAL02 协议
    """
    # 至少需要 11 字节
    if len(response_bytes) < 11:
        raise ValueError("响应报文长度不足")

    # 跳过地址、功能码、字节数
    data = response_bytes[3:]  # 从数据区开始
    # 提取高/低字节组合
    highest_point = (data[0] << 8) | data[1]
    lowest_point  = (data[2] << 8) | data[3]
    total_blocked = (data[4] << 8) | data[5]

    # 计算遮挡高度（假设光栅间距 2.5mm）
    height_mm = (total_blocked - 1) * 2.5 if total_blocked > 0 else 0

    return {
        'highest_point': highest_point,
        'lowest_point': lowest_point,
        'total_blocked': total_blocked,
        'height_mm': height_mm,
        'raw_hex': ' '.join(f'{b:02X}' for b in response_bytes)
    }

# ---------- 主处理函数 ----------
def process_param(param_dict):
    """
    核心算法：根据 param_dict 进行处理并返回数据
    param_dict 格式：
        {
            'algo': 'modbus_protocol',
            'method': 'build_command',
            'param': b'\x01\x03\x00\x00\x00\x03\xcb\x05'
        }
    """
    # 1. 验证字段
    algo = param_dict.get('algo')
    method = param_dict.get('method')
    request = param_dict.get('param')
    if algo != 'modbus_protocol' or method != 'build_command':
        raise ValueError("不支持的 algo 或 method")

    # 2. 模拟生成响应报文
    response_bytes = build_mock_response(request)

    # 3. 解析响应并返回结构化数据
    result = parse_modbus_response(response_bytes)
    return result

# ---------- 使用示例 ----------
if __name__ == '__main__':
    # 您传入的字典
    param_dict = {
        'algo': 'modbus_protocol',
        'method': 'build_command',
        'param': b'\x01\x03\x00\x00\x00\x03\xcb\x05'
    }

    # 调用算法
    result = process_param(param_dict)
    print("解析结果：")
    for key, val in result.items():
        print(f"  {key}: {val}")