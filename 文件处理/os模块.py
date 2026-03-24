import os

# 1. 获取文件大小（字节）
file_size = os.path.getsize('text.txt')
print(f"text.txt的大小：{file_size} 字节")

# 2. 重命名文件
os.rename('old_name.txt', 'new_name.txt')
print("文件重命名完成")

# 3. 删除文件
if os.path.exists('delete_me.txt'):  # 先判断文件是否存在，避免报错
    os.remove('delete_me.txt')
    print("文件已删除")
else:
    print("文件不存在，无需删除")

# 4. 判断文件是否存在
if os.path.isfile('test.txt'):
    print("test.txt是一个文件且存在")