## Q2 - ADD ALL THE LEAF NODES OF THE BST

class Node:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(node, key):
    if node is None:
        return Node(key)

    if key < node.key:
        node.left = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)

    return node

def search(root, key):
    if root is None or root.key == key:
        return root

    if root.key < key:
        return search(root.right, key)

    return search(root.left, key)

def sum_leaf_nodes(node):
    if node is None:
        return 0

    if node.left is None and node.right is None:
        return node.key

    return sum_leaf_nodes(node.left) + sum_leaf_nodes(node.right)

if __name__ == '__main__':
    root = None
    root = insert(root, 50)
    insert(root, 10)
    insert(root, 8)
    insert(root, 7)         # Leaf Node
    insert(root, 9)         # Leaf Node
    insert(root, 20)
    insert(root, 15)        # Leaf Node
    insert(root, 21)        # Leaf Node

    key = int(input("Enter The Node to be Searched : "))

    if search(root, key) is None:
        print(key, "NOT FOUND")
    else:
        print(key, "FOUND")

    sum_leaf = sum_leaf_nodes(root)
    print("Sum of Leaf Nodes :", sum_leaf)
