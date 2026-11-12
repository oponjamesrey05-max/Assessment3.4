"""Graph - Breadth-First Search

(0:O) --- (1:P) --- (2:N) --- (3:O)
"""
from collections import deque

labels = {0: "O", 1: "P", 2: "P", 3: "O"}
graph = {
    0: [1],
    1: [0, 2],
    2: [1, 3],
    3: [2],
}


def bfs(graph, start):
    visited = {start}
    queue = deque([start])
    result = []
    while queue:
        vertex = queue.popleft()
        result.append(labels[vertex])
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return result


print("Graph BFS:", " - ".join(bfs(graph, 0)))  # O - P - N - O