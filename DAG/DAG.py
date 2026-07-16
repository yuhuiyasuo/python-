from abc import ABC, abstractmethod
import networkx as nx


class BaseNode(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def execute(self):
        pass


class PythonNode(BaseNode):
    def __init__(self, name, func):
        super().__init__(name)
        self.func = func

    def execute(self):
        print(f"执行 {self.name}")
        self.func()


# 创建图
dag = nx.DiGraph()

download = PythonNode("Download", lambda: print("下载数据"))
clean = PythonNode("Clean", lambda: print("清洗数据"))
train = PythonNode("Train", lambda: print("训练模型"))

# 添加节点对象
dag.add_nodes_from([download, clean, train])

# 添加依赖
dag.add_edge(download, clean)
dag.add_edge(clean, train)

# 执行
if nx.is_directed_acyclic_graph(dag):
    for node in nx.topological_sort(dag):
        node.execute()