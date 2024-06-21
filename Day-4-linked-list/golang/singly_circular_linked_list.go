class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        # Create a new node with the given data
        new_node = Node(data)
        # If the list is empty, initialize the head to the new node and make it point to itself
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        # Traverse to the last node
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        # Insert the new node at the end and update the last node to point to the new node
        temp.next = new_node
        new_node.next = self.head

    def insert_at_beginning(self, data):
        # Create a new node with the given data
        new_node = Node(data)
        # Initialize a temporary variable to traverse the list
        temp = self.head
        new_node.next = self.head
        # If the list is empty, make the new node point to itself
        if not self.head:
            new_node.next = new_node
        else:
            # Traverse to the last node
            while temp.next != self.head:
                temp = temp.next
            # Update the last node to point to the new node
            temp.next = new_node
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
        for _ in range(position - 1):
            if temp.next == self.head:
                print("Position is greater than the length of the list.")
                return
            temp = temp.next
        # Insert the new node and update pointers
        new_node.next = temp.next
        temp.next = new_node

    def delete_node(self, key):
        if self.head is None:
            return
        temp = self.head
        # If the head node itself holds the key to be deleted
        if temp.data == key:
            # If there's only one node in the list
            if temp.next == self.head:
                self.head = None
            else:
                # Traverse to the last node
                while temp.next != self.head:
                    temp = temp.next
                # Update the last node to point to the next of head and update head
                temp.next = self.head.next
                self.head = self.head.next
            return
        prev = None
        # Search for the key to be deleted, keep track of the previous node
        while temp.next != self.head and temp.data != key:
            prev = temp
            temp = temp.next
        # Unlink the node from the linked list
        if temp.data == key:
            prev.next = temp.next
            temp = None

    def print_list(self):
        temp = self.head
        # Traverse through the list and print each node's data
        if self.head is not None:
            while True:
                print(temp.data, end=' ')
                temp = temp.next
                if temp == self.head:
                    break
        print()

# Usage
cllist = CircularLinkedList()
cllist.insert_at_end(1)
cllist.insert_at_end(2)
cllist.insert_at_beginning(0)
cllist.print_list()  # Output: 0 1 2
cllist.delete_node(1)
cllist.print_list()  # Output: 0 2
cllist.insert_at_position(1, 1)
cllist.print_list()  # Output: 0 1 2
