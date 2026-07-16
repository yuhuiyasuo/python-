#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Modbus TCP 客户端写入测试
支持功能：写单个寄存器、写多个寄存器、写单个线圈、写多个线圈
通过回读验证写入结果
"""

from pymodbus.client import ModbusTcpClient
import logging

# 启用日志便于调试（可选）
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.INFO)   # 改为 DEBUG 可查看更多细节


def modbus_write_test(host="127.0.0.1", port=502, slave_id=1):

    client = ModbusTcpClient(host, port)

    if not client.connect():
        print("❌ 无法连接到 Modbus 服务器，请检查 IP 和端口")
        return

    print(f"✅ 已连接到 {host}:{port}，从站 ID = {slave_id}\n")

    try:
        # ---------- 1. 写单个寄存器 (Holding Register) ----------
        reg_addr = 0
        reg_value = 1234
        print(f"[测试1] 写单个寄存器 地址={reg_addr} 值={reg_value}")
        result = client.write_register(reg_addr, reg_value, slave=slave_id)
        if result.isError():
            print(f"   ❌ 写入失败: {result}")
        else:
            # 回读验证
            read = client.read_holding_registers(reg_addr, 1, slave=slave_id)
            if not read.isError():
                print(f"   ✅ 回读成功: {read.registers[0]}")
            else:
                print(f"   ❌ 回读失败: {read}")

        # ---------- 2. 写多个寄存器 ----------
        reg_addr2 = 10
        reg_values = [11, 22, 33]
        print(f"\n[测试2] 写多个寄存器 地址={reg_addr2} 值={reg_values}")
        result = client.write_registers(reg_addr2, reg_values, slave=slave_id)
        if result.isError():
            print(f"   ❌ 写入失败: {result}")
        else:
            read = client.read_holding_registers(reg_addr2, len(reg_values), slave=slave_id)
            if not read.isError():
                print(f"   ✅ 回读成功: {read.registers}")
            else:
                print(f"   ❌ 回读失败: {read}")

        # ---------- 3. 写单个线圈 (Coil) ----------
        coil_addr = 0
        coil_value = True
        print(f"\n[测试3] 写单个线圈 地址={coil_addr} 值={coil_value}")
        result = client.write_coil(coil_addr, coil_value, slave=slave_id)
        if result.isError():
            print(f"   ❌ 写入失败: {result}")
        else:
            read = client.read_coils(coil_addr, 1, slave=slave_id)
            if not read.isError():
                print(f"   ✅ 回读成功: {read.bits[0]}")
            else:
                print(f"   ❌ 回读失败: {read}")

        # ---------- 4. 写多个线圈 ----------
        coil_addr2 = 5
        coil_values = [True, False, True]
        print(f"\n[测试4] 写多个线圈 地址={coil_addr2} 值={coil_values}")
        result = client.write_coils(coil_addr2, coil_values, slave=slave_id)
        if result.isError():
            print(f"   ❌ 写入失败: {result}")
        else:
            read = client.read_coils(coil_addr2, len(coil_values), slave=slave_id)
            if not read.isError():
                print(f"   ✅ 回读成功: {read.bits}")
            else:
                print(f"   ❌ 回读失败: {read}")

    except Exception as e:
        print(f"\n⚠️ 发生异常: {e}")
    finally:
        client.close()
        print("\n🔌 连接已关闭")


if __name__ == "__main__":
    # 使用默认参数连接本地模拟服务器，可根据实际修改
    modbus_write_test()