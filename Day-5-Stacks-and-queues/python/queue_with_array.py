class QueueArray:
    def __init__(self, size):
        # Initialize the queue with a given size
        self.queue = [None] * size  # Create a list with 'size' elements, all set to None
        self.front_index = 0  # Initialize front pointer to 0
        self.rear_index = -1  # Initialize rear pointer to -1, indicating the queue is empty
        self.size = size  # Store the size of the queue
        self.count = 0  # Initialize count of elements in the queue to 0

    def enqueue(self, item):
        if self.count == self.size:  # Check if the queue is full
            print("Queue Overflow")  # Print an overflow message
            return  # Exit the function
        self.rear_index = (self.rear_index + 1) % self.size  # Move rear pointer to the next position, wrapping around if necessary
        self.queue[self.rear_index] = item  # Insert the new item at the rear position
        self.count += 1  # Increment the count of elements in the queue

    def dequeue(self):
        if self.count == 0:  # Check if the queue is empty
            print("Queue Underflow")  # Print an underflow message
            return None  # Exit the function with None
        item = self.queue[self.front_index]  # Retrieve the item from the front position
        self.queue[self.front_index] = None  # Clear the item from the queue
        self.front_index = (self.front_index + 1) % self.size  # Move front pointer to the next position, wrapping around if necessary
        self.count -= 1  # Decrement the count of elements in the queue
        return item  # Return the dequeued item

    def get_front(self):
        if self.count == 0:  # Check if the queue is empty
            print("Queue is empty")  # Print an empty queue message
            return None  # Exit the function with None
        return self.queue[self.front_index]  # Return the item at the front position

    def get_rear(self):
        if self.count == 0:  # Check if the queue is empty
            print("Queue is empty")  # Print an empty queue message
            return None  # Exit the function with None
        return self.queue[self.rear_index]  # Return the item at the rear position

    def is_empty(self):
        return self.count == 0  # Return True if the queue is empty, otherwise False

    def is_full(self):
        return self.count == self.size  # Return True if the queue is full, otherwise False

# Usage example
queue = QueueArray(5)  # Create a queue of size 5

# Enqueue items
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)

# Check if the queue is full
print("Is the queue full?", queue.is_full())  # Output: Is the queue full? True

# Dequeue items
print("Dequeued item:", queue.dequeue())  # Output: Dequeued item: 10
print("Dequeued item:", queue.dequeue())  # Output: Dequeued item: 20

# Check front and rear items
print("Front item:", queue.get_front())  # Output: Front item: 30
print("Rear item:", queue.get_rear())    # Output: Rear item: 50

# Check if the queue is empty
print("Is the queue empty?", queue.is_empty())  # Output: Is the queue empty? False

# Enqueue more items
queue.enqueue(60)
queue.enqueue(70)

# Check front and rear items again
print("Front item:", queue.get_front())  # Output: Front item: 30
print("Rear item:", queue.get_rear())    # Output: Rear item: 70

# Try to enqueue when the queue is full
queue.enqueue(80)  # Output: Queue Overflow
