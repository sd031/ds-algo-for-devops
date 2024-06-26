class DeploymentStack:
    def __init__(self):
        self.stack = []

    def deploy(self, version):
        # Push the new version onto the stack
        self.stack.append(version)
        print(f"Deployed version: {version}")

    def rollback(self):
        # Check if the stack is empty (underflow condition)
        if not self.stack:
            print("No versions to rollback")
            return None
        # Pop the top version from the stack
        version = self.stack.pop()
        print(f"Rolled back version: {version}")
        return version

    def peek(self):
        # Check if the stack is empty
        if not self.stack:
            print("No versions available")
            return None
        # Return the topmost version without removing it
        return self.stack[-1]

    def is_empty(self):
        # Check if the stack is empty
        return len(self.stack) == 0

    def size(self):
        # Return the number of versions in the stack
        return len(self.stack)

# Usage Example
deployment_stack = DeploymentStack()

# Deploying versions
deployment_stack.deploy("v1.0")
deployment_stack.deploy("v1.1")
deployment_stack.deploy("v1.2")

# Peeking the top version
print(f"Current version: {deployment_stack.peek()}")  # Should print "Current version: v1.2"

# Checking the size of the stack
print(f"Total deployed versions: {deployment_stack.size()}")  # Should print "Total deployed versions: 3"

# Rolling back versions
deployment_stack.rollback()  # Should print "Rolled back version: v1.2"
deployment_stack.rollback()  # Should print "Rolled back version: v1.1"

# Checking if the stack is empty
print(f"Is the stack empty? {deployment_stack.is_empty()}")  # Should print "Is the stack empty? False"

# Rolling back the last version
deployment_stack.rollback()  # Should print "Rolled back version: v1.0"

# Checking if the stack is empty again
print(f"Is the stack empty? {deployment_stack.is_empty()}")  # Should print "Is the stack empty? True"

# Trying to rollback when there are no versions
deployment_stack.rollback()  # Should print "No versions to rollback"
