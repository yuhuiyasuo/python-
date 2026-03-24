# 定义重载装饰器的核心逻辑
def overload(func):
    """简单的重载装饰器：根据参数类型/个数分发逻辑"""
    # 存储不同参数规则对应的函数
    func_map = {}

    def register(*arg_types):  #这个参数在外面就是提取的装饰器中的参数（int，int）
        """注册器：绑定“参数类型”和“处理函数”"""
        def wrapper(f):
            func_map[arg_types] = f
            print(func_map)
            return f
        return wrapper

    def dispatcher(*args):
        """分发器：根据传入参数的类型，匹配对应的处理函数"""
        # 获取参数的类型元组（如 (int, int)、(list, str)）
        arg_types = tuple(type(arg) for arg in args)
        # 匹配对应的处理函数，匹配不到则执行原函数（或抛错）
        if arg_types in func_map:
            return func_map[arg_types](*args)
        else:
            raise TypeError(f"不支持的参数类型：{arg_types}")

    # 因为返回的dispatch，所以需要绑定register属性，以至于外部能直接访问
    dispatcher.register = register
    # 初始时把原函数作为默认逻辑（可选）
    func_map[tuple()] = func
    return dispatcher

# 1. 定义重载的核心函数名
@overload
def add():
    raise TypeError("请传入有效参数")

# 2. 注册不同参数类型的处理逻辑，这一步实在执行register中的方法
@add.register(int, int)
def _add_int(a, b):
    """处理两个整数相加"""
    return a + b

@add.register(list, str)
def _add_list(lst, elem):
    """处理列表追加元素"""
    new_lst = lst.copy()
    new_lst.append(elem)
    return new_lst

@add.register(str, str)
def _add_str(a, b):
    """处理两个字符串拼接"""
    return a + b

# 测试重载效果
if __name__ == "__main__":

    #实际调用的时候执行的是dispatch中的方法
    print(add(10, 20))                # 输出：30（匹配int,int）
    print(add(["a", "b"], "c"))       # 输出：['a', 'b', 'c']（匹配list,str）
    print(add("hello, ", "world"))    # 输出：hello, world（匹配str,str）
    # add(10, "20")  # 抛出TypeError：不支持的参数类型：(int, str)