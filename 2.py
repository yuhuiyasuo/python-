import asyncio
import logging
from pymodbus.server import ModbusTcpServer
from pymodbus.datastore import (
    ModbusSequentialDataBlock,
    ModbusSlaveContext,
    ModbusServerContext
)

# -------------------------- 日志配置 --------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S"
)
logging.getLogger("pymodbus").setLevel(logging.INFO)

# 全局保存从站上下文，用于后台读取寄存器状态
slave_ctx = None


# -------------------------- 寄存器快照打印 --------------------------
async def print_register_snapshot():
    """后台协程：每秒打印一次保持寄存器快照，直观展示写入的数据变化"""
    print("\n📊 保持寄存器快照将每秒自动刷新\n")
    while True:
        if slave_ctx:
            # 读取 地址0~59 的保持寄存器值
            hr_values = slave_ctx.store['h'].getValues(0, count=60)
            print("=" * 85)
            print(f"地址 00-19: {hr_values[0:20]}")
            print(f"地址 20-39: {hr_values[20:40]}")
            print(f"地址 40-59: {hr_values[40:60]}")
            print("=" * 85)
        await asyncio.sleep(1)


# -------------------------- 服务端主逻辑 --------------------------
async def run_modbus_server():
    global slave_ctx

    # 1. 初始化4种标准Modbus存储区，各100个地址，初始值全为0
    slave_ctx = ModbusSlaveContext(
        hr=ModbusSequentialDataBlock(0, [0] * 100),  # 保持寄存器 → 功能码 03读 / 16写
        co=ModbusSequentialDataBlock(0, [0] * 100),  # 线圈 → 功能码 01读 / 15写
        di=ModbusSequentialDataBlock(0, [0] * 100),  # 离散输入 → 功能码 02读
        ir=ModbusSequentialDataBlock(0, [0] * 100),  # 输入寄存器 → 功能码 04读
        unit=0  # 从站地址，和客户端测试代码保持一致
    )

    # 2. 创建服务端全局上下文
    server_context = ModbusServerContext(slaves=slave_ctx, single=True)

    # 3. 启动后台快照打印协程
    asyncio.create_task(print_register_snapshot())

    # 4. 启动TCP服务端
    server = ModbusTcpServer(
        context=server_context,
        address=("0.0.0.0", 502)
    )

    print("✅ Modbus TCP 模拟服务端启动成功")
    print("📍 监听端口: 502    从站地址: 0")
    print("💡 运行客户端测试脚本后，观察下方寄存器数值变化即可验证写入效果\n")

    await server.serve_forever()


if __name__ == "__main__":
    try:
        asyncio.run(run_modbus_server())
    except PermissionError:
        print("\n❌ 权限错误：Windows系统502端口需要管理员权限")
        print("解决方案：以管理员身份运行终端，或把端口改为 5020（同步修改客户端port参数）")
    except OSError as e:
        print(f"\n❌ 启动失败: {e}")
        print("大概率是端口被占用，请更换端口号")
