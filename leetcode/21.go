package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func NewListNode(value int) *ListNode {
	return &ListNode{Val: value}
}

func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
	dummy := NewListNode(0)
	current := dummy
	for list1 != nil && list2 != nil {
		if list1.Val < list2.Val {
			current.Next = list1
			list1 = list1.Next
		} else {
			current.Next = list2
			list2 = list2.Next
		}

		current = current.Next
	}

	if list1 != nil {
		current.Next = list1
	}

	if list2 != nil {
		current.Next = list2
	}

	return dummy.Next
}

func CreateList(values []int) *ListNode {
	dummy := NewListNode(0)
	current := dummy

	for _, v := range values {
		current.Next = NewListNode(v)
		current = current.Next
	}

	return dummy.Next
}

func IterateList(list *ListNode) {
	for list != nil {
		println(list.Val)
		list = list.Next
	}
}

func main() {
	list1 := CreateList([]int{1, 3, 5, 11, 19})
	list2 := CreateList([]int{2, 4, 6, 8, 10})

	list3 := mergeTwoLists(list1, list2)
	IterateList(list3)
}
