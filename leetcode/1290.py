"""
https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, _next=None):
        self.val = val
        self.next = _next


def getDecimalValue(head: ListNode) -> int:
    data = list()

    current = head
    while current:
        data.append(str(current.val))
        current = current.next

    return int(''.join(data), 2)


def getDecimalValue(head: ListNode) -> int:
    ans = 0
    while head:
        ans = 2 * ans + head.val
        head = head.next
    return ans

