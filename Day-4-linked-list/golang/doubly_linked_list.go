package main

import "fmt"

type Node struct {
	data int
	prev *Node
	next *Node
}

type DoublyLinkedList struct {
	head *Node
}

func (dll *DoublyLinkedList) InsertAtBeginning(data int) {
	newNode := &Node{data: data}
	newNode.next = dll.head
	if dll.head != nil {
		dll.head.prev = newNode
	}
	dll.head = newNode
}

func (dll *DoublyLinkedList) InsertAtEnd(data int) {
	newNode := &Node{data: data}
	if dll.head == nil {
		dll.head = newNode
		return
	}
	last := dll.head
	for last.next != nil {
		last = last.next
	}
	last.next = newNode
	newNode.prev = last
}

func (dll *DoublyLinkedList) InsertAtPosition(position, data int) {
	if position < 0 {
		fmt.Println("Position can't be negative.")
		return
	}
	newNode := &Node{data: data}
	if position == 0 {
		newNode.next = dll.head
		if dll.head != nil {
			dll.head.prev = newNode
		}
		dll.head = newNode
		return
	}
	temp := dll.head
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
	newNode.prev = temp
	if temp.next != nil {
		temp.next.prev = newNode
	}
	temp.next = newNode
}

func (dll *DoublyLinkedList) DeleteNode(key int) {
	temp := dll.head
	if temp != nil && temp.data == key {
		dll.head = temp.next
		if dll.head != nil {
			dll.head.prev = nil
		}
		temp = nil
		return
	}
	for temp != nil && temp.data != key {
		temp = temp.next
	}
	if temp == nil {
		return
	}
	if temp.next != nil {
		temp.next.prev = temp.prev
	}
	if temp.prev != nil {
		temp.prev.next = temp.next
	}
	temp = nil
}

func (dll *DoublyLinkedList) PrintListForward() {
	temp := dll.head
	for temp != nil {
		fmt.Print(temp.data, " ")
		temp = temp.next
	}
	fmt.Println()
}

func (dll *DoublyLinkedList) PrintListBackward() {
	temp := dll.head
	if temp == nil {
		return
	}
	for temp.next != nil {
		temp = temp.next
	}
	for temp != nil {
		fmt.Print(temp.data, " ")
		temp = temp.prev
	}
	fmt.Println()
}

func main() {
	dllist := &DoublyLinkedList{}
	dllist.InsertAtEnd(1)
	dllist.InsertAtEnd(2)
	dllist.InsertAtBeginning(0)
	dllist.PrintListForward()  // Output: 0 1 2
	dllist.PrintListBackward() // Output: 2 1 0
	dllist.DeleteNode(1)
	dllist.PrintListForward() // Output: 0 2
	dllist.InsertAtPosition(1, 1)
	dllist.PrintListForward()  // Output: 0 1 2
	dllist.PrintListBackward() // Output: 2 1 0
}
