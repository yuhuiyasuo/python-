import json


class SetDecoder(json.JSONDecoder):

    # 1. 初始化：绑定钩子函数
    '''
    什么是钩子（hook）？ 系统自动调用的函数
    就是：
    每次解析到一个字典 {} 时，先自动调用我这个函数
    这行的意思：
    爸爸（父类），你解析 JSON 时，每个字典都先丢给我处理
    '''
    def __init__(self, *args, **kwargs):
        json.JSONDecoder.__init__(self, object_hook=self.object_hook, *args, **kwargs)

    # 2. 钩子函数：解析每个字典时触发

    def object_hook(self, obj):
        # 这里的逻辑取决于您如何标记原始集合
        # 例如，您可能有特定的键或特定的值结构
        if 'is_set' in obj:
            return set(obj['values'])
        return obj


def set_default(obj):
    if isinstance(obj, set):
        # 返回字典，而不是直接返回列表
        return {
            "is_set": True,
            "values": list(obj)
        }
    raise TypeError



s = {1, 2, 3}

json_str = json.dumps(s, default=set_default)
print(json_str)

data = json.loads(json_str, cls=SetDecoder)
print(data)
print(type(data))




import json

# 这就是钩子函数：系统自动调用，不用你手动跑
def my_hook(obj):
    print("钩子被调用了！解析到字典：", obj)
    return obj

# 主流程：json解析
data = json.loads('{"a":1}', object_hook=my_hook)



# 这是我们自己写的【普通函数】
# 它接收一个参数 hook —— 这个就是【钩子函数】
def do_something(hook=None):
    print("我是主函数，开始执行任务...")

    # ======================
    # 关键：这里自动调用钩子！
    # 你不用手动调，系统/函数自己调
    # ======================
    if hook is not None:
        print("→ 触发钩子函数！")
        hook()  # 调用传进来的钩子

    print("主函数任务执行完毕！")


# ----------------------
# 下面是：我们自己写的钩子
# ----------------------
def my_hook():
    print("我是钩子函数，被自动调用啦！")


# ----------------------
# 使用：把钩子传给函数
# ----------------------
do_something(hook=my_hook)

# 我是主函数，开始执行任务...
# → 触发钩子函数！
# 我是钩子函数，被自动调用啦！
# 主函数任务执行完毕！