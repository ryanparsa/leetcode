# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        def bfs(node):
            if not node:
                return node

            stack = [node]

            while stack:
                n = stack.pop()

        return bfs(node)
