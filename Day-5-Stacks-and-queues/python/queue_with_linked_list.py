class Node:
    def __init__(self, value):
        # Initialize a node with a given value and no next node
        self.value = value  # Store the value of the node
        self.next = None  # Initialize the next pointer to None

class QueueLinkedList:
    def __init__(self):
        # Initialize an empty queue
        self.front = None  # The front pointer of the queue, initially None
        self.rear = None  # The rear pointer of the queue, initially None

    def enqueue(self, item):
        new_node = Node(item)  # Create a new node with the given item
        if self.rear is None:  # Check if the queue is empty
            self.front = self.rear = new_node  # Set both front and rear to the new node
            return
        self.rear.next = new_node  # Link the new node to the end of the queue
        self.rear = new_node  # Update the rear pointer to the new node

    def dequeue(self):
        if self.front is None:  # Check if the queue is empty
            print("Queue Underflow")  # Print an underflow message
            return None  # Exit the function with None
        item = self.front.value  # Retrieve the value from the front node
        self.front = self.front.next  # Move the front pointer to the next node
        if self.front is None:  # If the queue is now empty
            self.rear = None  # Set the rear pointer to None
        return item  # Return the dequeued item

    def get_front(self):
        if self.front is None:  # Check if the queue is empty
            print("Queue is empty")  # Print an empty queue message
            return None  # Exit the function with None
        return self.front.value  # Return the value at the front node

    def get_rear(self):
        if self.rear is None:  # Check if the queue is empty
            print("Queue is empty")  # Print an empty queue message
            return None  # Exit the function with None
        return self.rear.value  # Return the value at the rear node

    def is_empty(self):
        return self.front is None  # Return True if the queue is empty, otherwise False

# Usage example
queue = QueueLinkedList()  # Create a new QueueLinkedList instance

# Enqueue items
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)

# Check if the queue is empty
print("Is the queue empty?", queue.is_empty())  # Output: Is the queue empty? False

# Check front and rear items
print("Front item:", queue.get_front())  # Output: Front item: 10
print("Rear item:", queue.get_rear())    # Output: Rear item: 50

# Dequeue items
print("Dequeued item:", queue.dequeue())  # Output: Dequeued item: 10
print("Dequeued item:", queue.dequeue())  # Output: Dequeued item: 20

# Check front and rear items again
print("Front item:", queue.get_front())  # Output: Front item: 30
print("Rear item:", queue.get_rear())    # Output: Rear item: 50

# Dequeue more items
print("Dequeued item:", queue.dequeue())  # Output: Dequeued item: 30
print("Dequeued item:", queue.dequeue())  # Output: Dequeued item: 40
print("Dequeued item:", queue.dequeue())  # Output: Dequeued item: 50

# Check if the queue is empty after dequeuing all items
print("Is the queue empty?", queue.is_empty())  # Output: Is the queue empty? True

# Try to dequeue from an empty queue
print("Dequeued item:", queue.dequeue())  # Output: Queue Underflow
                                         #          Dequeued item: None
