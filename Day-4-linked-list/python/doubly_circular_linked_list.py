class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        # Create a new node with the given data
        new_node = Node(data)
        # If the list is empty, initialize the head to the new node and make it circular
        if not self.head:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
            return
        # Get the last node (previous of the head)
        last = self.head.prev
        # Insert the new node at the end and update pointers
        last.next = new_node
        new_node.prev = last
        new_node.next = self.head
        self.head.prev = new_node

    def insert_at_beginning(self, data):
        # Create a new node with the given data
        new_node = Node(data)
        # If the list is empty, initialize the head to the new node and make it circular
        if not self.head:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            # Get the last node (previous of the head)
            last = self.head.prev
            # Insert the new node at the beginning and update pointers
            new_node.next = self.head
            new_node.prev = last
            self.head.prev = new_node
            last.next = new_node
        # Update the head to be the new node
        self.head = new_node

    def insert_at_position(self, position, data):
        # Ensure the position is not negative
        if position < 0:
            print("Position can't be negative.")
            return
        # Create a new node with the given data
        new_node = Node(data)
        # If inserting at the head, handle separately
        if position == 0:
            self.insert_at_beginning(data)
            return
        # Traverse to the node just before the desired position
        temp = self.head
        for _ in range(position):
            temp = temp.next
            if temp == self.head:
                print("Position is greater than the length of the list.")
                return
        # Insert the new node and update pointers
        new_node.next = temp
        new_node.prev = temp.prev
        temp.prev.next = new_node
        temp.prev = new_node

    def delete_node(self, key):
        if self.head is None:
            return
        temp = self.head
        # Search for the key to be deleted
        while temp.data != key:
            temp = temp.next
            if temp == self.head:
                return
        # If the list has only one node
        if temp.next == self.head and temp.prev == self.head:
            self.head = None
            return
        # If the node to be deleted is the head
        if temp == self.head:
            self.head = temp.next
        # Unlink the node from the linked list
        temp.prev.next = temp.next
        temp.next.prev = temp.prev
        temp = None

    def print_list(self):
        if self.head is None:
            return
        temp = self.head
        # Traverse through the list and print each node's data
        while True:
            print(temp.data, end=' ')
            temp = temp.next
            if temp == self.head:
                break
        print()

# Usage
cdllist = CircularDoublyLinkedList()
cdllist.insert_at_end(1)
cdllist.insert_at_end(2)
cdllist.insert_at_beginning(0)
cdllist.print_list()  # Output: 0 1 2
cdllist.delete_node(1)
cdllist.print_list()  # Output: 0 2
cdllist.insert_at_position(1, 1)
cdllist.print_list()  # Output: 0 1 2
