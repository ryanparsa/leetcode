import random
import timeit


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def __str__(self):
        return str(self.val)


def insert(root, key):
    if not root or root.val is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root


def bfs(root):
    if root is None:
        return

    queue = [root]
    while queue:
        current = queue.pop(0)
        print(current.val, end=" ")

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)


def dfs_inorder(root):
    if root:
        dfs_inorder(root.left)
        print(root.val, end=" ")
        dfs_inorder(root.right)


def dfs_preorder(root):
    if root:
        print(root.val, end=" ")
        dfs_preorder(root.left)
        dfs_preorder(root.right)


def dfs_postorder(root):
    if root:
        dfs_postorder(root.left)
        dfs_postorder(root.right)
        print(root.val, end=" ")


def max_depth(root) -> int:
    if not root:
        return 0

    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)

    return 1 + max(left_depth, right_depth)


if __name__ == "__main__":
    # Creating the root node
    root_node = None
    values_to_insert = [3, 9, 20, None, None, 15, 7]

    for value in values_to_insert:
        root_node = insert(root_node, value)

    print(max_depth(root_node))
