"""Graph - Depth-First Search

(0:O) --- (1:P) --- (2:N) --- (3:O)
"""

labels = {0: "O", 1: "P", 2: "N", 3: "O"}
graph = {
    0: [1],
    1: [0, 2],
    2: [1, 3],
    3: [2],
}


def dfs(graph, vertex, visited=None, result=None):
    if visited is None:
        visited, result = set(), []
    visited.add(vertex)
    result.append(labels[vertex])
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, result)
    return result


print("Graph DFS:", " - ".join(dfs(graph, 0)))  # O - P - N - O