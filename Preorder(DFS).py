# DFS Preorder Traversal: Root -> Left -> Right
#
# BINARY TREE:
#
#               J
#             /   \
#            A     M
#           / \   / \
#          E   S O   P
#         / \
#        O   N
#
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def preorder(node, result):
    if node is not None:
        result.append(node.data)
        preorder(node.left, result)
        preorder(node.right, result)
    return result


# Build the tree
root = Node("J")
root.left = Node("A")
root.right = Node("M")
root.left.left = Node("E")
root.left.right = Node("S")
root.left.left.left = Node("O")
root.left.left.right = Node("N")
root.right.left = Node("O")
root.right.right = Node("P")

print("Preorder:", " -> ".join(preorder(root, [])))