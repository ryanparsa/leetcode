from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"val: {self.val}, left: {self.left}, right: {self.right}"

    def __str__(self) -> str:
        return str(self.val)


def maxDepth(root: Optional[TreeNode]) -> int:
    pass


def create_tree(values: list[int]) -> TreeNode:


r = create_tree([3, 9, 20, None, None, 15, 7])
