"""
https://leetcode.com/problems/merge-two-sorted-lists/
"""
from typing import Optional


class ListNode:
    def __init__(self, val: int, _next=None):
        self.val = val
        self.next = _next

    def __str__(self):
        return f'{self.val}'


def create_list(values: list[int]):
    dummy = None
    current = dummy

    for i in values:
        if not current:
            dummy = ListNode(i)
            current = dummy
        else:
            current.next = ListNode(i)
            current = current.next

    return dummy


def iterate_list(head: ListNode):
    while head:
        print(head.val, end=', ')
        head = head.next

    print()


def merge(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(-1, None)
    current = dummy

    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    if l1:
        current.next = l1
    if l2:
        current.next = l2

    return dummy.next


if __name__ == '__main__':
    list1 = create_list([1, 3, 5, 11, 19])
    list2 = create_list([2, 4, 6, 8, 10])

    list3 = merge(list1, list2)
    iterate_list(list3)
