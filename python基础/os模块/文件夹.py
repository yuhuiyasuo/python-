# 1. 获取当前工作目录（CWD）
import os

current_dir = os.getcwd()
print("当前工作目录：", current_dir)

# 2. 切换工作目录
# os.chdir("/Users/xxx/Documents")  # 绝对路径（Mac/Linux）
# os.chdir("D:\\xxx\\Documents")    # 绝对路径（Windows，注意转义）
# os.chdir("../")                   # 相对路径（上级目录）

# 3. 创建目录
os.mkdir("new_dir")  # 创建单个目录，若已存在会报错
os.makedirs("parent/child/grandchild")  # 递归创建多级目录，更实用

# 4. 删除目录
os.rmdir("new_dir")  # 删除空的单个目录
os.removedirs("parent/child/grandchild")  # 递归删除空目录（仅当子目录都为空时）

# 5. 列出目录下的所有文件/子目录
files = os.listdir(current_dir)
print("当前目录下的内容：", files)

# 6. 遍历目录（含子目录）+ 判断路径类型（推荐结合os.walk）
for root, dirs, files in os.walk(current_dir):
    print(f"当前目录：{root}")
    print(f"子目录列表：{dirs}")
    print(f"文件列表：{files}")
    print("-" * 20)



# 1. 重命名文件/目录（通用）
# 先创建测试文件
with open("test.txt", "w") as f:
    f.write("test content")
os.rename("test.txt", "new_test.txt")  # 重命名，路径需正确

# 2. 删除文件（注意：不可逆，谨慎使用）
os.remove("new_test.txt")

# 3. 判断文件/目录是否存在
print("文件是否存在：", os.path.exists("new_test.txt"))  # 输出: False
print("目录是否存在：", os.path.exists("parent"))        # 根据实际情况输出