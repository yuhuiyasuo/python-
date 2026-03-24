def check_permission(allowed_roles):
    def decorator(func):

        def wrapper(user_role, *args, **kwargs):
            if user_role in allowed_roles:
                print(f"角色 {user_role} 有权限执行 {func.__name__}")
                return func(*args, **kwargs)
            else:
                raise PermissionError(f"角色 {user_role} 无权限！")
        return wrapper
    return decorator

# 使用
@check_permission(allowed_roles=["admin", "editor"])
def edit_article(title):
    return f"文章《{title}》编辑成功"

# 有权限调用
print(edit_article("admin", "Python装饰器详解"))  # 正常执行   此时的edit_article相当于wrapper(user_role, *args, **kwargs)

#===================与上面的内容等价==========================
# # 1. 调用装饰器工厂，传入allowed_roles，返回decorator函数
# temp_decorator = check_permission(allowed_roles=["admin", "editor"])
# # 2. 调用decorator，传入原edit_article函数，返回wrapper函数
# edit_article = temp_decorator(edit_article)

# 无权限调用
try:
    edit_article("guest", "Python入门")
except PermissionError as e:
    print(e)  # 输出：角色 guest 无权限！