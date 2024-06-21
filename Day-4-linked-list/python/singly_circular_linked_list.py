package main

import "fmt"

type Node struct {
	data int
	next *Node
}

type CircularLinkedList struct {
	head *Node
}

func (cll *CircularLinkedList) InsertAtEnd(data int) {
	newNode := &Node{data: data}
	if cll.head == nil {
		cll.head = newNode
		newNode.next = cll.head
		return
	}
	temp := cll.head
	for temp.next != cll.head {
		temp = temp.next
	}
	temp.next = newNode
	newNode.next = cll.head
}

func (cll *CircularLinkedList) InsertAtBeginning(data int) {
	newNode := &Node{data: data}
	if cll.head == nil {
		cll.head = newNode
		newNode.next = newNode
	} else {
		temp := cll.head
		newNode.next = cll.head
		for temp.next != cll.head {
			temp = temp.next
		}
		temp.next = newNode
		cll.head = newNode
	}
}

func (cll *CircularLinkedList) InsertAtPosition(position, data int) {
	if position < 0 {
		fmt.Println("Position can't be negative.")
		return
	}
	if position == 0 {
		cll.InsertAtBeginning(data)
		return
	}
	newNode := &Node{data: data}
	temp := cll.head
	for i := 0; i < position-1; i++ {
		if temp.next == cll.head {
			fmt.Println("Position is greater than the length of the list.")
			return
		}
		temp = temp.next
	}
	newNode.next = temp.next
	temp.next = newNode
}

func (cll *CircularLinkedList) DeleteNode(key int) {
	if cll.head == nil {
		return
	}
	temp := cll.head
	if cll.head.data == key {
		if cll.head.next == cll.head {
			cll.head = nil
		} else {
			for temp.next != cll.head {
				temp = temp.next
			}
			temp.next = cll.head.next
			cll.head = cll.head.next
		}
		return
	}
	var prev *Node
	for temp.next != cll.head && temp.data != key {
		prev = temp
		temp = temp.next
	}
	if temp.data == key {
		prev.next = temp.next
	}
}

func (cll *CircularLinkedList) PrintList() {
	if cll.head == nil {
		return
	}
	temp := cll.head
	for {
		fmt.Print(temp.data, " ")
		temp = temp.next
		if temp == cll.head {
			break
		}
	}
	fmt.Println()
}

func main() {
	cllist := &CircularLinkedList{}
	cllist.InsertAtEnd(1)
	cllist.InsertAtEnd(2)
	cllist.InsertAtBeginning(0)
	cllist.PrintList() // Output: 0 1 2
	cllist.DeleteNode(1)
	cllist.PrintList() // Output: 0 2
	cllist.InsertAtPosition(1, 1)
	cllist.PrintList() // Output: 0 1 2
}
