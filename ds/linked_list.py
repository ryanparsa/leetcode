from typing import Self


class Node:
    def __init__(self, value: int, next_node: Self = None):
        self.value: int = value
        self.next: Node = next_node

    def __str__(self):
        return str(self.value)

    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other: 'Node') -> bool:
        return self.value == other.value


class LinkedList:
    __slots__ = ('head', 'tail', '__current_node')

    def __init__(self, head: Node = None, tail: Node = None):
        self.head: Node = head
        self.tail: Node = tail

        self.__current_node: Node | None = None

    def __str__(self):
        if self.is_empty():
            return f'{self.__class__.__name__} Empty'
        return f'{self.__class__.__name__} {self.head} {self.tail}'

    def __len__(self):
        return self.length()

    def __iter__(self):
        """
        Initialize the iterator by returning itself.
        """
        self.__current_node = self.head
        return self

    def __next__(self):
        """
        Get the next element in the linked list.
        """
        if self.__current_node is None:
            raise StopIteration
        else:
            value = self.__current_node.value
            self.__current_node = self.__current_node.next
            return value

    def is_empty(self) -> bool:
        return not self.head

    def wipe(self) -> None:
        """
        Clear all elements from the linked list.
        """
        self.head = None
        self.tail = None
        self.__current_node = None

    def append_after(self, node: Node, value: Node):
        pass

    def append_before(self, node: Node, value: Node):
        pass

    def append_right(self, value: int) -> None:
        new_node = Node(value)

        if self.tail:
            self.tail.next = new_node
            self.tail = new_node

        else:
            self.head = new_node
            self.tail = new_node

    def append_left(self, value: int) -> None:
        new_node = Node(value)
        if self.head:
            new_node.next = self.head
            self.head = new_node

    def search(self, value: int) -> Node:
        """
        search in a disorder linked list
        :param value:
        :return:
        """
        if self.is_empty():
            raise IndexError('ll is empty')

        current: Node = self.head
        while current:
            if current.value == value:
                return current
            current = current.next

        raise IndexError('value is not in list')

    def as_dict(self) -> dict:
        """
        Convert the linked list to a dictionary.
        """
        result = {}

        current = self.head
        while current:
            result[current.value] = current
            current = current.next

        return result

    def remove(self, value: int):
        pass

    def bubble_sort(self):
        """
        Sort nodes in linked list by value using the bubble sort algorithm.
        :return:
        """
        if self.is_empty():
            raise IndexError('ll is empty')

        # Traverse the linked list
        current = self.head
        while current:
            # Inner loop to compare and swap values
            inner_current = self.head
            while inner_current.next:
                if inner_current.value > inner_current.next.value:
                    # Swap values
                    inner_current.value, inner_current.next.value = inner_current.next.value, inner_current.value
                inner_current = inner_current.next
            current = current.next

    def reverse(self):
        """
        reverse nodes in linked by swapping next and prev link
        :return:
        """

    def traverse(self) -> list[int]:
        if self.is_empty():
            raise IndexError('ll is empty')

        result = list()

        current = self.head
        while current:
            result.append(current.value)
            current = current.next

        return result

    def length(self) -> int:
        if self.is_empty():
            raise IndexError('ll is empty')

        counter: int = 0
        current: Node = self.head

        while current:
            counter += 1
            current = current.next

        return counter

    def pop_left(self) -> Node:
        if self.is_empty():
            raise IndexError('tail is empty')
        current = self.head
        self.head = self.head.next
        current.next = None

        return current

    def pop_right(self) -> Node:
        if self.is_empty():
            raise IndexError('head is empty')

        current = self.tail

        current.prev.next = None
        current.prev = None

        return current


ll = LinkedList()

ll.append_right(7)
ll.append_right(2)
ll.append_right(3)
ll.append_right(1)
ll.append_right(5)
ll.append_right(6)
ll.append_right(4)

ll.append_left(0)

for i in ll:
    print(i)

ll.bubble_sort()

for i in ll:
    print(i)

print(ll.as_dict())
