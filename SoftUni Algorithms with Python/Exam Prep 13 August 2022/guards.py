def dfs(node, graph, visited):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor, graph, visited)


N = int(input())
M = int(input())
edges = [list(map(int, input().split())) for _ in range(M)]
start_node = int(input())

graph = [[] for _ in range(N + 1)]
for edge in edges:
    graph[edge[0]].append(edge[1])

visited = [False] * (N + 1)
dfs(start_node, graph, visited)

# Print unreachable nodes
unreachable_nodes = [node for node in range(1, N + 1) if not visited[node]]
nodes_list = []
for node in unreachable_nodes:
    nodes_list.append(node)

print(*nodes_list, sep=" ")
