class Node:
    def __init__(self, key: any):
        self.left = None
        self.right = None
        self.val = key

    def __str__(self):
        return str(self.val)


def bfs(root: Node):
    if not root:
        return root

    stack = [root]

    while stack:
        node = stack.pop()
        print(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)


def dfs(root: Node):
    if not root:
        return root

    print(root.val)
    dfs(root.left)
    dfs(root.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

bfs(root)
dfs(root)
