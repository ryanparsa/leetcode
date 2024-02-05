# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        c = 0

        node = head

        while node:
            c += 1
            node = node.next

        i = c // 2 + 1

        for z in range(1, i + 1):
            if z == i:
                return head
            else:
                head = head.next

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        mid = end = head
        while end and end.next:
            end = end.next.next
            mid = mid.next
        return mid
