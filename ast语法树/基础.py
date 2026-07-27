#AST（Abstract Syntax Tree，抽象语法树）是 Python 内置 `ast` 模块的核心能力，
# 它的本质是：**将符合 Python 语法的源代码字符串，转化为一棵结构化、带类型的树形节点对象**

import ast

code = "a = b + 1"

tree = ast.parse(code)

print(tree)
print(ast.dump(tree))
print(ast.dump(tree, indent=4))

import ast

code = """
print("hello")
sum([1,2,3])
"""

tree = ast.parse(code)
print(ast.dump(tree))
print(ast.dump(tree, indent=4))


code = "write_register(address=0, value=11, slave=1)"

tree = ast.parse(code)
print(ast.dump(tree))
print(ast.dump(tree, indent=4))