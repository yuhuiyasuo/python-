import json


class SetDecoder(json.JSONDecoder):

    # 1. 初始化：绑定钩子函数
    '''
    什么是钩子（hook）？
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