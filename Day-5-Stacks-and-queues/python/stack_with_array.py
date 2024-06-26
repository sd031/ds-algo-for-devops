class StackArray:
    def __init__(self, size):
        # Initialize the stack with a fixed size
        self.stack = [None] * size
        # The top attribute keeps track of the index of the topmost element
        self.top = -1
        # The size attribute holds the maximum capacity of the stack
        self.size = size

    def push(self, item):
        # Check if the stack is full (overflow condition)
        if self.top >= self.size - 1:
            print("Stack Overflow")
            return
        # Increment the top index to point to the new topmost element
        self.top += 1
        # Add the new item to the top of the stack
        self.stack[self.top] = item

    def pop(self):
        # Check if the stack is empty (underflow condition)
        if self.top == -1:
            print("Stack Underflow")
            return None
        # Retrieve the topmost item
        item = self.stack[self.top]
        # Remove the topmost item by setting it to None
        self.stack[self.top] = None
        # Decrement the top index to point to the new topmost element
        self.top -= 1
        # Return the popped item
        return item

    def peek(self):
        # Check if the stack is empty
        if self.top == -1:
            print("Stack is empty")
            return None
        # Return the topmost item without removing it
        return self.stack[self.top]

    def is_empty(self):
        # Check if the stack is empty
        return self.top == -1

    def is_full(self):
        # Check if the stack is full
        return self.top == self.size - 1

# Usage Example
stack = StackArray(5)

# Pushing elements onto the stack
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)

# Trying to push an element onto a full stack
stack.push(60)  # Should print "Stack Overflow"

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
