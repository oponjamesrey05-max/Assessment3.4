"""Binary Tree - Depth-First Search (preorder: root, left, right)

        O        Level 0
       / \
      P   O      Level 1
     /
    N            Level 2
"""

class Node:
    def __init__(self, label):
        self.label = label
        self.left = None
        self.right = None


def dfs(node, result=None):
    if result is None:
        result = []
    if node is None:
        return result
    result.append(node.label)  # visit root
    dfs(node.left, result)  # then left subtree
    dfs(node.right, result)  # then right subtree
    return result


root = Node("O")
root.left = Node("P")
root.right = Node("O")
root.left.left = Node("N")

print("Binary Tree DFS:", " - ".join(dfs(root)))  # O - P - N - O