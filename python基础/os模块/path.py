# 1. 路径拼接（核心！避免手动拼/或\，适配不同系统）
import os

path1 = "parent_dir"
path2 = "child_dir"
full_path = os.path.join(path1, path2, "file.txt")
print("拼接后的路径：", full_path)
# Mac/Linux输出: parent_dir/child_dir/file.txt
# Windows输出: parent_dir\child_dir\file.txt

# 2. 拆分路径（目录+文件名）
dir_name, file_name = os.path.split(full_path)
print("目录部分：", dir_name)   # 输出: parent_dir/child_dir
print("文件名部分：", file_name)  # 输出: file.txt

# 3. 拆分文件名和扩展名
file_base, file_ext = os.path.splitext(file_name)
print("文件名（无后缀）：", file_base)  # 输出: file
print("扩展名：", file_ext)            # 输出: .txt

# 4. 判断路径类型
test_path = os.getcwd()
print("是否为绝对路径：", os.path.isabs(test_path))    # 输出: True
print("是否为目录：", os.path.isdir(test_path))        # 输出: True
print("是否为文件：", os.path.isfile(test_path))       # 输出: False

# 5. 获取文件大小（字节）
# with open("test_size.txt", "w") as f:
#     f.write("123456789")
# print("文件大小：", os.path.getsize("test_size.txt"))  # 输出: 9