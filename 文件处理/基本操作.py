
# 打开文件（只读模式），使用with语句自动关闭文件（最佳实践）
with open('text.txt', mode='r', encoding='utf-8') as f:
    # 读取全部内容
    content = f.read()
    print("文件全部内容：")
    print(content)


with open('text.txt', mode='r', encoding='utf-8') as f:
    lines = f.readlines()
    print("文件内容按行存为列表：")
    print(lines)  # 每行末尾会保留\n，格式如：['第一行\n', '第二行\n']



# # 写入模式：w
# with open('output.txt', mode='w', encoding='utf-8') as f:
#     # 写入单行内容
#     f.write("这是覆盖写入的内容\n")
#     # 写入多行内容（列表格式）
#     lines = ["第二行内容\n", "第三行内容\n"]
#     f.writelines(lines)
# print("写入完成，output.txt已生成/覆盖")
#
#
# # 追加模式：a
# with open('output.txt', mode='a', encoding='utf-8') as f:
#     f.write("这是追加的内容\n")
# print("追加完成，output.txt末尾新增内容")





#===========================对二进制文件进行操作

# # 读取二进制文件（图片）
# with open('source.jpg', mode='rb') as f_read:
#     # 读取所有二进制内容
#     img_data = f_read.read()
#
# # 写入二进制文件（复制图片）
# with open('copy.jpg', mode='wb') as f_write:
#     f_write.write(img_data)
#
# print("图片复制完成，生成copy.jpg")
