import json

# 定义普通 Python 字典
data = {
    "name": "张三",
    "age": 25,
    "is_student": False,
    "hobbies": ["读书", "跑步"],
    "address": {"city": "北京", "district": "朝阳"}
}

# 字典转 JSON 字符串
json_str = json.dumps(data)

dic_str = json.loads(json_str)
print(type(json_str))  # <class 'str'>
print(json_str)
# 输出（默认 ASCII 编码，中文会转义）：
# {"name": "\u5f20\u4e09", "age": 25,
# "is_student": false,
# "hobbies": ["\u8bfb\u4e66", "\u8dd1\u6b65"],
# "address": {"city": "\u5317\u4eac", "district": "\u671d\u9633"}}


import json

data = {"name": "张三", "age": 25}

# # 将字典写入 test.json 文件
# with open("test.json", "w", encoding="utf-8") as f:
#     json.dump(data, f)  # 写入文件，默认同样会转义中文