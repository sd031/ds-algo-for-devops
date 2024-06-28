class Node:
    def __init__(self, value):
        self.value = value      # Initialize the value of the node
        self.next = None        # Initialize the next pointer of the node as None

class QueueLinkedList:
    def __init__(self):
        self.front = None       # Initialize the front pointer of the queue as None
        self.rear = None        # Initialize the rear pointer of the queue as None

    def enqueue(self, item):
        new_node = Node(item)   # Create a new node with the given item
        if self.rear is None:   # If the queue is empty (rear is None)
            self.front = self.rear = new_node  # Set both front and rear to the new node
            return
        self.rear.next = new_node  # Link the new node at the end of the queue
        self.rear = new_node        # Update the rear to point to the new node

    def dequeue(self):
        if self.front is None:   # If the queue is empty (front is None)
            print("Queue Underflow")  # Print an underflow message
            return None          # Return None indicating the queue is empty
        item = self.front.value  # Retrieve the value of the front node
        self.front = self.front.next  # Move the front pointer to the next node
        if self.front is None:   # If the queue becomes empty after the dequeue operation
            self.rear = None     # Set the rear pointer to None
        return item              # Return the dequeued item

    def front_value(self):
        if self.front is None:   # If the queue is empty (front is None)
            print("Queue is empty")  # Print an empty message
            return None          # Return None indicating the queue is empty
        return self.front.value  # Return the value at the front of the queue

    def rear_value(self):
        if self.rear is None:    # If the queue is empty (rear is None)
            print("Queue is empty")  # Print an empty message
            return None          # Return None indicating the queue is empty
        return self.rear.value   # Return the value at the rear of the queue

    def is_empty(self):
        return self.front is None  # Return True if the front is None (queue is empty)

class MessageQueue:
    def __init__(self):
        self.queue = QueueLinkedList()  # Initialize the queue as a linked list queue

    def send_message(self, message):
        self.queue.enqueue(message)  # Enqueue the message to the queue
        print(f"Message sent: {message}")  # Print the sent message

    def receive_message(self):
        message = self.queue.dequeue()  # Dequeue a message from the queue
        if message:  # If a message was dequeued
            print(f"Message received: {message}")  # Print the received message
        return message  # Return the received message

    def is_empty(self):
        return self.queue.is_empty()  # Check if the queue is empty

# Example usage
message_queue = MessageQueue()  # Create a new MessageQueue instance
message_queue.send_message("Service A: Task 1")  # Send a message
message_queue.send_message("Service B: Task 2")  # Send another message
message_queue.receive_message()  # Receive a message (should be "Service A: Task 1")
message_queue.receive_message()  # Receive another message (should be "Service B: Task 2")
message_queue.receive_message()  # Try to receive another message (should indicate queue underflow)
