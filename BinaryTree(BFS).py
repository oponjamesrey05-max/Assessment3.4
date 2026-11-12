"""Binary Tree - Breadth-First Search (level order)

        O        Level 0
       / \
      P   O      Level 1
     /
    N            Level 2
"""

from collections import deque


class Node:
    def __init__(self, label):
        self.label = label
        self.left = None
        self.right = None


def bfs(root):
    result = []
    if root is None:
        return result
    queue = deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.label)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result


root = Node("O")
root.left = Node("P")
root.right = Node("O")
root.left.left = Node("N")

print("Binary Tree BFS:", " - ".join(bfs(root)))