import networkx as nx


def print_title(title):
    """打印标题"""
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


# =====================================================
# 1. 创建有向图
# =====================================================

print_title("1. 创建 DiGraph")

G = nx.DiGraph()

print(type(G))


# =====================================================
# 2. 添加节点
# =====================================================

print_title("2. add_node()")

G.add_node("Download")
G.add_node("Clean")

print("当前节点：")
print(list(G.nodes))


# =====================================================
# 3. 添加带属性的节点
# =====================================================

print_title("3. 节点属性")

G.add_node(
    "Train",
    retry=3,
    timeout=60,
    owner="Tom"
)

print("Train节点属性：")
print(G.nodes["Train"])


# =====================================================
# 4. 批量添加节点
# =====================================================

print_title("4. add_nodes_from()")

G.add_nodes_from([
    "Feature",
    "Evaluate",
    "Deploy"
])

print(list(G.nodes))


# =====================================================
# 5. 添加边（依赖关系）
# =====================================================

print_title("5. add_edge()")

G.add_edge("Download", "Clean")
G.add_edge("Clean", "Feature")

print(list(G.edges))


# =====================================================
# 6. 批量添加边
# =====================================================

print_title("6. add_edges_from()")

G.add_edges_from([
    ("Download", "Validate"),
    ("Validate", "Feature"),
    ("Feature", "Train"),
    ("Train", "Evaluate"),
    ("Evaluate", "Deploy")
])

print(list(G.edges))


# =====================================================
# 7. 添加边属性
# =====================================================

print_title("7. 边属性")

G.add_edge(
    "Deploy",
    "Finish",
    weight=10,
    retry=False
)

print(G["Deploy"]["Finish"])


# =====================================================
# 8. 查看所有节点
# =====================================================

print_title("8. nodes()")

print(list(G.nodes))

print("\n带属性：")

print(G.nodes(data=True))


# =====================================================
# 9. 查看所有边
# =====================================================

print_title("9. edges()")

print(list(G.edges))

print("\n带属性：")

print(G.edges(data=True))


# =====================================================
# 10. 查询节点
# =====================================================

print_title("10. has_node()")

print(G.has_node("Train"))
print(G.has_node("ABC"))


# =====================================================
# 11. 查询边
# =====================================================

print_title("11. has_edge()")

print(G.has_edge("Download", "Clean"))
print(G.has_edge("Clean", "Deploy"))


# =====================================================
# 12. successors()
# =====================================================

print_title("12. successors()")

print("Download 的后继节点：")

print(list(G.successors("Download")))


# =====================================================
# 13. predecessors()
# =====================================================

print_title("13. predecessors()")

print("Feature 的前驱节点：")

print(list(G.predecessors("Feature")))


# =====================================================
# 14. 入度
# =====================================================

print_title("14. in_degree()")

print("Feature 入度：")

print(G.in_degree("Feature"))


# =====================================================
# 15. 出度
# =====================================================

print_title("15. out_degree()")

print("Download 出度：")

print(G.out_degree("Download"))


# =====================================================
# 16. 总度
# =====================================================

print_title("16. degree()")

print("Feature 总度：")

print(G.degree("Feature"))


# =====================================================
# 17. 图信息
# =====================================================

print_title("17. 图信息")

print("节点数量：", G.number_of_nodes())

print("边数量：", G.number_of_edges())


# =====================================================
# 18. 判断是否为 DAG
# =====================================================

print_title("18. is_directed_acyclic_graph()")

print(nx.is_directed_acyclic_graph(G))


# =====================================================
# 19. 拓扑排序（工作流执行顺序）
# =====================================================

print_title("19. topological_sort()")

order = list(nx.topological_sort(G))

print(order)


# =====================================================
# 20. 复制图
# =====================================================

print_title("20. copy()")

copy_graph = G.copy()

print(copy_graph.nodes)


# =====================================================
# 21. 反转图
# =====================================================

print_title("21. reverse()")

reverse_graph = G.reverse()

print(list(reverse_graph.edges))


# =====================================================
# 22. 子图
# =====================================================

print_title("22. subgraph()")

sub = G.subgraph([
    "Download",
    "Clean",
    "Feature"
])

print(list(sub.nodes))

print(list(sub.edges))


# =====================================================
# 23. 删除边
# =====================================================

print_title("23. remove_edge()")

temp = G.copy()

temp.remove_edge("Download", "Clean")

print(list(temp.edges))


# =====================================================
# 24. 删除节点
# =====================================================

print_title("24. remove_node()")

temp = G.copy()

temp.remove_node("Validate")

print(list(temp.nodes))

print(list(temp.edges))


# =====================================================
# 25. 构造一个有环图
# =====================================================

print_title("25. DAG检测")

cycle = nx.DiGraph()

cycle.add_edges_from([
    ("A", "B"),
    ("B", "C"),
    ("C", "A")
])

print("是否为DAG：")

print(nx.is_directed_acyclic_graph(cycle))


# =====================================================
# 26. 最终 DAG 示意
# =====================================================

print_title("26. 最终工作流")

workflow = nx.DiGraph()

workflow.add_edges_from([
    ("Download", "Clean"),
    ("Download", "Validate"),
    ("Clean", "Feature"),
    ("Validate", "Feature"),
    ("Feature", "Train"),
    ("Train", "Evaluate"),
    ("Evaluate", "Deploy")
])

print("节点：")

print(list(workflow.nodes))

print("\n边：")

print(list(workflow.edges))

print("\n拓扑排序：")

print(list(nx.topological_sort(workflow)))

print("\n按拓扑顺序执行：")

for node in nx.topological_sort(workflow):
    print(f"执行：{node}")