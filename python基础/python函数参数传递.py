def reassign_list(lst):
    lst = [4, 5, 6]      # 创建新列表，lst 指向新对象
    print(f"函数内: lst = {lst}")

def modify_list(lst):
    lst[0] = 999         # 修改原对象
    print(f"函数内: lst = {lst}")

my_list = [1, 2, 3]

# 情况1：重新绑定
reassign_list(my_list)
print(f"函数外: my_list = {my_list}")  # [1, 2, 3]，未改变

# 情况2：修改
modify_list(my_list)
print(f"函数外: my_list = {my_list}")  # [999, 2, 3]，被修改



def modify_num(x):
    print(f"函数内的id{id(x)}")
    x = x + 10  # 创建了一个新的整数对象  不可变对象不能够修改本身，所以会创建一个新对象
    print(f"函数内的id{id(x)}")
    print(f"函数内: x = {x}")

num = 5
print(f"函数外的id{id(num)}")
modify_num(num)

print(f"函数外: num = {num}")  # 仍然是 5

# 输出：
# 函数内: x = 15
# 函数外: num = 5