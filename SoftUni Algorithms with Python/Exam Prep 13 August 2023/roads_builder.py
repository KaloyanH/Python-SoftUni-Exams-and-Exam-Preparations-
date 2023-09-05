class Edge:
    def __init__(self, first, second, weight, critical):
        self.first = first
        self.second = second
        self.weight = weight
        self.critical = critical


def find_root(parent, node):
    while node != parent[node]:
        node = parent[node]
    return node


edges = int(input())
graph = []
city_indices = {}

index_counter = 0

for _ in range(edges):
    input_args = input().split(' ')
    if len(input_args) == 3:
        first, second, weight = input_args
        critical = False
    else:
        first, second, weight, critical = input_args

    if first not in city_indices:
        city_indices[first] = index_counter
        index_counter += 1
    if second not in city_indices:
        city_indices[second] = index_counter
        index_counter += 1

    graph.append(Edge(city_indices[first], city_indices[second], int(weight), critical))

critical_edges = [edge for edge in graph if edge.critical]
non_critical_edges = [edge for edge in graph if not edge.critical]

parent = {node: node for node in range(index_counter + 1)}
critical_forest = []

critical_total_distance = 0
for edge in sorted(critical_edges, key=lambda e: e.weight):
    first_node_root = find_root(parent, edge.first)
    second_node_root = find_root(parent, edge.second)

    if first_node_root != second_node_root:
        parent[first_node_root] = second_node_root
        critical_forest.append(edge)
        critical_total_distance += edge.weight

total_distance = critical_total_distance
for edge in sorted(non_critical_edges, key=lambda e: e.weight):
    first_node_root = find_root(parent, edge.first)
    second_node_root = find_root(parent, edge.second)

    if first_node_root != second_node_root:
        parent[first_node_root] = second_node_root
        total_distance += edge.weight

print(total_distance)
