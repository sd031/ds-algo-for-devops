package main

import "fmt"

type Node struct {
	data int
	next *Node
}

type LinkedList struct {
	head *Node
}

func (ll *LinkedList) InsertAtBeginning(data int) {
	newNode := &Node{data: data}
	newNode.next = ll.head
	ll.head = newNode
}

func (ll *LinkedList) InsertAtEnd(data int) {
	newNode := &Node{data: data}
	if ll.head == nil {
		ll.head = newNode
		return
	}
	last := ll.head
	for last.next != nil {
		last = last.next
	}
	last.next = newNode
}

func (ll *LinkedList) InsertAtPosition(position int, data int) {
	if position < 0 {
		fmt.Println("Position can't be negative.")
		return
	}
	newNode := &Node{data: data}
	if position == 0 {
		newNode.next = ll.head
		ll.head = newNode
		return
	}
	temp := ll.head
	for i := 0; i < position-1; i++ {
		if temp == nil {
			fmt.Println("Position is greater than the length of the list.")
			return
		}
		temp = temp.next
	}
	if temp == nil {
		fmt.Println("Position is greater than the length of the list.")
		return
	}
	newNode.next = temp.next
	temp.next = newNode
}

func (ll *LinkedList) DeleteNode(key int) {
	temp := ll.head
	if temp != nil && temp.data == key {
		ll.head = temp.next
		temp = nil
		return
	}
	var prev *Node
	for temp != nil && temp.data != key {
		prev = temp
		temp = temp.next
	}
	if temp == nil {
		return
	}
	prev.next = temp.next
	temp = nil
}

func (ll *LinkedList) PrintList() {
	temp := ll.head
	for temp != nil {
		fmt.Print(temp.data, " ")
		temp = temp.next
	}
	fmt.Println()
}

func main() {
	llist := &LinkedList{}
	llist.InsertAtEnd(1)
	llist.InsertAtEnd(2)
	llist.InsertAtBeginning(0)
	llist.PrintList() // Output: 0 1 2
	llist.DeleteNode(1)
	llist.PrintList() // Output: 0 2
	llist.InsertAtPosition(1, 1)
	llist.PrintList() // Output: 0 1 2
}
