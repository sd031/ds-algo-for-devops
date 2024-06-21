class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        # Create a new node with the given data
        new_node = Node(data)
        # Point the new node's next to the current head
        new_node.next = self.head
        # Update the head to be the new node
        self.head = new_node

    def insert_at_end(self, data):
        # Create a new node with the given data
        new_node = Node(data)
        # If the list is empty, make the new node the head
        if not self.head:
            self.head = new_node
            return
        # Traverse to the end of the list
        last = self.head
        while last.next:
            last = last.next
        # Point the last node's next to the new node
        last.next = new_node

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
        # Point the current node's next to the new node
        temp.next = new_node

    def delete_node(self, key):
        temp = self.head
        # If the head node itself holds the key to be deleted
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return
        # Search for the key to be deleted, keep track of the previous node
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        # If the key is not present in the list
        if not temp:
            return
        # Unlink the node from the linked list
        prev.next = temp.next
        temp = None

    def print_list(self):
        temp = self.head
        # Traverse through the list and print each node's data
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
        print()

# Usage
llist = LinkedList()
llist.insert_at_end(1)
llist.insert_at_end(2)
llist.insert_at_beginning(0)
llist.print_list()  # Output: 0 1 2
llist.delete_node(1)
llist.print_list()  # Output: 0 2
llist.insert_at_position(1, 1)
llist.print_list()  # Output: 0 1 2
