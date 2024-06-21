class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        # Create a new node with the given data
        new_node = Node(data)
        # Point the new node's next to the current head
        new_node.next = self.head
        # If the list is not empty, update the current head's previous pointer to the new node
        if self.head is not None:
            self.head.prev = new_node
        # Update the head to be the new node
        self.head = new_node

    def insert_at_end(self, data):
        # Create a new node with the given data
        new_node = Node(data)
        # If the list is empty, make the new node the head
        if self.head is None:
            self.head = new_node
            return
        # Traverse to the end of the list
        last = self.head
        while last.next:
            last = last.next
        # Point the last node's next to the new node
        last.next = new_node
        # Point the new node's previous to the last node
        new_node.prev = last

    def insert_at_position(self, position, data):
        # Ensure the position is not negative
        if position < 0:
            print("Position can't be negative.")
            return
        # Create a new node with the given data
        new_node = Node(data)
        # If inserting at the head, handle separately
        if position == 0:
            new_node.next = self.head
            if self.head is not None:
                self.head.prev = new_node
            self.head = new_node
            return
        # Traverse to the node just before the desired position
        temp = self.head
        for _ in range(position - 1):
            if not temp:
                print("Position is greater than the length of the list.")
                return
            temp = temp.next
        # If reached end of the list before position, handle the error
        if not temp:
            print("Position is greater than the length of the list.")
            return
        # Point the new node's next to the current node's next
        new_node.next = temp.next
        # Point the new node's previous to the current node
        new_node.prev = temp
        # If the current node's next is not None, update its previous pointer to the new node
        if temp.next is not None:
            temp.next.prev = new_node
        # Point the current node's next to the new node
        temp.next = new_node

    def delete_node(self, key):
        temp = self.head
        # If the head node itself holds the key to be deleted
        if temp is not None and temp.data == key:
            self.head = temp.next
            if self.head is not None:
                self.head.prev = None
            temp = None
            return
        # Search for the key to be deleted
        while temp is not None and temp.data != key:
            temp = temp.next
        # If the key is not present in the list
        if temp is None:
            return
        # Unlink the node from the linked list
        if temp.next is not None:
            temp.next.prev = temp.prev
        if temp.prev is not None:
            temp.prev.next = temp.next
        temp = None

    def print_list_forward(self):
        temp = self.head
        # Traverse through the list and print each node's data
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
        print()

    def print_list_backward(self):
        temp = self.head
        # Traverse to the end of the list
        while temp and temp.next:
            temp = temp.next
        # Traverse backward through the list and print each node's data
        while temp:
            print(temp.data, end=' ')
            temp = temp.prev
        print()

# Usage
dllist = DoublyLinkedList()
dllist.insert_at_end(1)
dllist.insert_at_end(2)
dllist.insert_at_beginning(0)
dllist.print_list_forward()  # Output: 0 1 2
dllist.print_list_backward() # Output: 2 1 0
dllist.delete_node(1)
dllist.print_list_forward()  # Output: 0 2
dllist.insert_at_position(1, 1)
dllist.print_list_forward()  # Output: 0 1 2
dllist.print_list_backward() # Output: 2 1 0
