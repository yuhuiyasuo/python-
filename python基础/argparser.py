# 1. 导入argparse模块（内置模块，无需额外安装）
import argparse

def main():
    # 2. 创建ArgumentParser对象（解析器核心，可指定脚本描述）
    parser = argparse.ArgumentParser(description="这是一个argparse基础示例脚本，用于演示核心流程")

    # 3. 向解析器添加命令行参数（必选/可选参数都在这里定义）
    parser.add_argument("name", help="用户姓名（必选位置参数）")
    parser.add_argument("age", type=int, help="用户年龄（必选位置参数，整数类型）")

    # 4. 解析命令行传入的参数（返回命名空间对象，存储解析后的参数值）
    args = parser.parse_args()

    # 5. 使用解析后的参数（通过「args.参数名」访问）
    print(f"你好，{args.name}！你今年{args.age}岁了。")
    print("解析后的参数命名空间：", args)

if __name__ == "__main__":
    main()