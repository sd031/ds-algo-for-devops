package main

import "fmt"

type Node struct {
	data int
	prev *Node
	next *Node
}

type CircularDoublyLinkedList struct {
	head *Node
}

func (cdll *CircularDoublyLinkedList) InsertAtEnd(data int) {
	newNode := &Node{data: data}
	if cdll.head == nil {
		cdll.head = newNode
		newNode.next = newNode
		newNode.prev = newNode
		return
	}
	last := cdll.head.prev
	last.next = newNode
	newNode.prev = last
	newNode.next = cdll.head
	cdll.head.prev = newNode
}

func (cdll *CircularDoublyLinkedList) InsertAtBeginning(data int) {
	newNode := &Node{data: data}
	if cdll.head == nil {
		cdll.head = newNode
		newNode.next = newNode
		newNode.prev = newNode
	} else {
		last := cdll.head.prev
		newNode.next = cdll.head
		newNode.prev = last
		cdll.head.prev = newNode
		last.next = newNode
		cdll.head = newNode
	}
}

func (cdll *CircularDoublyLinkedList) InsertAtPosition(position int, data int) {
	if position < 0 {
		fmt.Println("Position can't be negative.")
		return
	}
	if position == 0 {
		cdll.InsertAtBeginning(data)
		return
	}
	newNode := &Node{data: data}
	temp := cdll.head
	for i := 0; i < position; i++ {
		temp = temp.next
		if temp == cdll.head {
			fmt.Println("Position is greater than the length of the list.")
			return
		}
	}
	newNode.next = temp
	newNode.prev = temp.prev
	temp.prev.next = newNode
	temp.prev = newNode
}

func (cdll *CircularDoublyLinkedList) DeleteNode(key int) {
	if cdll.head == nil {
		return
	}
	temp := cdll.head
	for temp.data != key {
		temp = temp.next
		if temp == cdll.head {
			return
		}
	}
	if temp.next == cdll.head && temp.prev == cdll.head {
		cdll.head = nil
		return
	}
	if temp == cdll.head {
		cdll.head = temp.next
	}
	temp.prev.next = temp.next
	temp.next.prev = temp.prev
}

func (cdll *CircularDoublyLinkedList) PrintList() {
	if cdll.head == nil {
		return
	}
	temp := cdll.head
	for {
		fmt.Print(temp.data, " ")
		temp = temp.next
		if temp == cdll.head {
			break
		}
	}
	fmt.Println()
}

func main() {
	cdllist := &CircularDoublyLinkedList{}
	cdllist.InsertAtEnd(1)
	cdllist.InsertAtEnd(2)
	cdllist.InsertAtBeginning(0)
	cdllist.PrintList() // Output: 0 1 2
	cdllist.DeleteNode(1)
	cdllist.PrintList() // Output: 0 2
	cdllist.InsertAtPosition(1, 1)
	cdllist.PrintList() // Output: 0 1 2
}
