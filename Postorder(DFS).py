# DFS Postorder Traversal: Left -> Right -> Root
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


def postorder(node, result):
    if node is not None:
        postorder(node.left, result)
        postorder(node.right, result)
        result.append(node.data)
    return result


# Build the binary tree
root = Node("J")
root.left = Node("A")
root.right = Node("M")
root.left.left = Node("E")
root.left.right = Node("S")
root.left.left.left = Node("O")
root.left.left.right = Node("N")
root.right.left = Node("O")
root.right.right = Node("P")

# Display the binary tree
print(r"""
BINARY TREE:

              J
            /   \
           A     M
          / \   / \
         E   S O   P
        / \
       O   N
""")

print("Postorder:", " -> ".join(postorder(root, [])))
