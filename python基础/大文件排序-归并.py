import os
from typing import List


def split_large_file(input_file: str, temp_dir: str, chunk_size: int = 100000, encoding: str = "utf-8") -> List[str]:
    """
    （与之前完全一致，无需修改）将超大文件分割为多个小临时文件，并对每个小文件进行内部排序
    :param input_file: 输入超大文件路径
    :param temp_dir: 临时文件存储目录
    :param chunk_size: 每个小文件的最大行数（可根据内存调整，默认10万行）
    :param encoding: 文件编码
    :return: 有序小临时文件的路径列表
    """
    # 确保临时目录存在
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)

    temp_file_paths = []
    chunk_count = 0
    current_chunk = []

    try:
        with open(input_file, "r", encoding=encoding) as f_in:
            for line in f_in:
                # 收集当前chunk的行数据
                current_chunk.append(line)

                # 当chunk达到指定大小，进行排序并写入临时文件
                if len(current_chunk) >= chunk_size:
                    chunk_count += 1
                    temp_file_path = os.path.join(temp_dir, f"temp_sorted_{chunk_count}.txt")

                    # 对当前chunk排序（数值排序可修改key参数）
                    sorted_chunk = sorted(current_chunk)

                    # 写入临时文件
                    with open(temp_file_path, "w", encoding=encoding, newline="") as f_temp:
                        f_temp.writelines(sorted_chunk)

                    # 记录临时文件路径
                    temp_file_paths.append(temp_file_path)

                    # 清空当前chunk，准备下一批数据
                    current_chunk = []

            # 处理最后一批不足chunk_size的数据
            if current_chunk:
                chunk_count += 1
                temp_file_path = os.path.join(temp_dir, f"temp_sorted_{chunk_count}.txt")
                sorted_chunk = sorted(current_chunk)
                with open(temp_file_path, "w", encoding=encoding, newline="") as f_temp:
                    f_temp.writelines(sorted_chunk)
                temp_file_paths.append(temp_file_path)

        print(f"文件分割与内部排序完成，生成{chunk_count}个有序临时文件")
        return temp_file_paths

    except Exception as e:
        print(f"文件分割失败：{str(e)}")
        # 清理已生成的临时文件
        for temp_file in temp_file_paths:
            if os.path.exists(temp_file):
                os.remove(temp_file)
        return []


def merge_sorted_temp_files_manual(temp_file_paths: List[str], output_file: str, encoding: str = "utf-8"):
    """
    （手动实现，不使用heapq.merge）归并多个有序临时文件，生成最终有序大文件
    :param temp_file_paths: 有序临时文件路径列表
    :param output_file: 输出最终排序文件路径
    :param encoding: 文件编码
    """
    if not temp_file_paths:
        print("无有序临时文件可归并")
        return

    temp_file_objects = []  # 存储所有打开的临时文件对象
    current_lines = []  # 存储每个临时文件的「当前行」，与文件对象列表一一对应，None表示文件已读完

    try:
        # 步骤1：打开所有临时文件，读取第一行作为初始当前行
        for temp_path in temp_file_paths:
            f_temp = open(temp_path, "r", encoding=encoding)
            temp_file_objects.append(f_temp)
            # 读取第一行，去除末尾换行符（可选，排序时不影响，统一格式）
            first_line = f_temp.readline()
            current_lines.append(first_line if first_line else None)

        # 步骤2：循环归并，直至所有文件的当前行都为None
        with open(output_file, "w", encoding=encoding, newline="") as f_out:
            while True:
                # 筛选有效数据：(当前行内容, 对应文件索引)，排除None的项
                valid_data = []
                for idx, line in enumerate(current_lines):
                    if line is not None and line.strip() != "":  # 过滤空行（可选，根据数据情况调整）
                        valid_data.append((line, idx))

                # 无有效数据，说明所有文件已读完，退出循环
                if not valid_data:
                    break

                # 步骤3：线性查找最小值（默认字符串字典序，数值排序需修改此处比较逻辑）
                # 若需降序，改为max(valid_data, key=lambda x: x[0])
                min_item = min(valid_data, key=lambda x: x[0])
                min_line, min_file_idx = min_item  # 最小值行内容、对应文件索引

                # 步骤4：将最小值写入最终文件
                f_out.write(min_line)

                # 步骤5：从对应文件读取下一行，更新当前行列表
                next_line = temp_file_objects[min_file_idx].readline()
                current_lines[min_file_idx] = next_line if next_line else None

        print(f"临时文件手动归并完成，最终结果已保存至：{output_file}")

    except Exception as e:
        print(f"临时文件手动归并失败：{str(e)}")

    finally:
        # 步骤6：关闭所有临时文件对象，释放资源
        for f_temp in temp_file_objects:
            if not f_temp.closed:
                f_temp.close()


def clean_temp_files(temp_file_paths: List[str], temp_dir: str):
    """
    （与之前完全一致，无需修改）清理临时文件和临时目录
    :param temp_file_paths: 临时文件路径列表
    :param temp_dir: 临时目录路径
    """
    try:
        for temp_file in temp_file_paths:
            if os.path.exists(temp_file):
                os.remove(temp_file)
        # 删除空的临时目录
        if os.path.exists(temp_dir) and not os.listdir(temp_dir):
            os.rmdir(temp_dir)
        print("临时文件清理完成")
    except Exception as e:
        print(f"临时文件清理失败：{str(e)}")


def sort_ultra_large_file_manual(input_file: str, output_file: str, temp_dir: str = "temp_sort_dir",
                                 chunk_size: int = 100000, encoding: str = "utf-8"):
    """
    （整合手动归并）排序远超内存容量的超大文件（外部排序）
    :param input_file: 输入超大文件路径
    :param output_file: 输出最终排序文件路径
    :param temp_dir: 临时文件存储目录
    :param chunk_size: 每个小临时文件的最大行数
    :param encoding: 文件编码
    """
    # 步骤1：分割并内部排序，得到有序临时文件列表
    temp_file_paths = split_large_file(input_file, temp_dir, chunk_size, encoding)
    if not temp_file_paths:
        return

    # 步骤2：手动归并有序临时文件（替换原heapq.merge实现）
    merge_sorted_temp_files_manual(temp_file_paths, output_file, encoding)

    # 步骤3：清理临时文件
    clean_temp_files(temp_file_paths, temp_dir)


# 调用示例
if __name__ == "__main__":
    INPUT_ULTRA_FILE = "ultra_large_data.txt"
    OUTPUT_ULTRA_FILE = "sorted_ultra_large_data_manual.txt"
    TEMP_DIR = "temp_sort_dir"
    CHUNK_SIZE = 200000  # 可根据内存大小调整

    sort_ultra_large_file_manual(INPUT_ULTRA_FILE, OUTPUT_ULTRA_FILE, TEMP_DIR, CHUNK_SIZE)