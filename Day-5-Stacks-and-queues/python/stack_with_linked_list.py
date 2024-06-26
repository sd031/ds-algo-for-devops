class Node:
    def __init__(self, value):
        # Initialize a node with a given value and next pointer set to None
        self.value = value
        self.next = None

class StackLinkedList:
    def __init__(self):
        # Initialize the stack with top set to None
        self.top = None

    def push(self, item):
        # Create a new node with the given item
        new_node = Node(item)
        # Set the next of the new node to the current top
        new_node.next = self.top
        # Update the top to the new node
        self.top = new_node

    def pop(self):
        # Check if the stack is empty (underflow condition)
        if self.top is None:
            print("Stack Underflow")
            return None
        # Retrieve the topmost item's value
        item = self.top.value
        # Update the top to the next node
        self.top = self.top.next
        # Return the popped item's value
        return item

    def peek(self):
        # Check if the stack is empty
        if self.top is None:
            print("Stack is empty")
            return None
        # Return the topmost item's value without removing it
        return self.top.value

    def is_empty(self):
        # Check if the stack is empty
        return self.top is None

# Usage Example
stack = StackLinkedList()

# Pushing elements onto the stack
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)

# Peeking the top element
print(f"Top element is: {stack.peek()}")  # Should print "Top element is: 50"

# Popping elements from the stack
print(f"Popped element is: {stack.pop()}")  # Should print "Popped element is: 50"
print(f"Popped element is: {stack.pop()}")  # Should print "Popped element is: 40"

# Checking if the stack is empty
print(f"Is the stack empty? {stack.is_empty()}")  # Should print "Is the stack empty? False"

# Popping all elements to make the stack empty
stack.pop()  # Popping 30
stack.pop()  # Popping 20
stack.pop()  # Popping 10

# Checking if the stack is empty again
print(f"Is the stack empty? {stack.is_empty()}")  # Should print "Is the stack empty? True"

# Trying to pop from an empty stack
print(f"Popped element is: {stack.pop()}")  # Should print "Stack Underflow" and return None
