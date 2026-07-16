import subprocess
import sys
import os


def check_root() -> None:
    """检查是否拥有 root 权限，修改系统时间必须 root 身份"""
    if os.geteuid() != 0:
        print("错误：修改 Linux 系统时间需要 root 权限")
        print("请使用 sudo 运行脚本：sudo python3 脚本文件名.py")
        sys.exit(1)


def get_current_time() -> str:
    """获取当前系统时间字符串"""
    result = subprocess.run(
        ["date", "+%Y-%m-%d %H:%M:%S"],
        capture_output=True,
        text=True,
        check=True
    )
    return result.stdout.strip()


def set_system_time(time_str: str) -> None:
    """设置系统时间"""
    subprocess.run(
        ["date", "-s", time_str],
        check=True,
        capture_output=True,
        text=True
    )


if __name__ == "__main__":
    # 1. 权限校验
    check_root()

    # 2. 记录原始正确时间（用于后续恢复）
    original_time = get_current_time()
    print("=" * 40)
    print(f"原始系统时间：{original_time}")
    print("=" * 40)
    print()

    # 3. 修改为自定义测试时间
    test_time = "2024-01-01 12:00:00"  # 可自行修改为任意时间
    try:
        set_system_time(test_time)
        modified_time = get_current_time()
        print("=" * 40)
        print(f"已修改为测试时间：{modified_time}")
        print("=" * 40)
    except subprocess.CalledProcessError as e:
        print(f"修改时间失败：{e.stderr.strip()}")
        sys.exit(1)
    print()

    # 4. 恢复回原始时间
    try:
        set_system_time(original_time)
        restored_time = get_current_time()
        print("=" * 40)
        print(f"已恢复原始时间：{restored_time}")
        print("=" * 40)
    except subprocess.CalledProcessError as e:
        print(f"恢复时间失败：{e.stderr.strip()}")
        sys.exit(1)
