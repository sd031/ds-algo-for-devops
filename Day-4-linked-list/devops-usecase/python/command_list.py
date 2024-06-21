import subprocess

class CommandNode:
    def __init__(self, command):
        self.command = command
        self.status = None  # None: not executed, True: success, False: failure
        self.output = None
        self.error = None
        self.prev = None
        self.next = None

class CommandList:
    def __init__(self):
        self.head = None

    def add_command(self, command):
        # Create a new command node with the given command
        new_node = CommandNode(command)
        # If the list is empty, initialize the head to the new node
        if not self.head:
            self.head = new_node
        else:
            # Traverse to the end of the list
            temp = self.head
            while temp.next:
                temp = temp.next
            # Insert the new node at the end and update pointers
            temp.next = new_node
            new_node.prev = temp

    def execute_commands(self):
        temp = self.head
        # Traverse through the list and execute each command
        while temp:
            try:
                # Run the command using subprocess and capture the output
                result = subprocess.run(temp.command, shell=True, text=True, capture_output=True, check=True)
                temp.status = True
                temp.output = result.stdout
                temp.error = result.stderr
                print(f"Command '{temp.command}' succeeded.")
            except subprocess.CalledProcessError as e:
                temp.status = False
                temp.output = e.stdout
                temp.error = e.stderr
                print(f"Command '{temp.command}' failed with error: {e.stderr.strip()}")
            temp = temp.next

    def print_commands_status(self):
        temp = self.head
        # Traverse through the list and print the status of each command
        while temp:
            status = "Success" if temp.status else "Failure" if temp.status is not None else "Not Executed"
            print(f"Command: {temp.command}, Status: {status}")
            if temp.output:
                print(f"Output: {temp.output.strip()}")
            if temp.error:
                print(f"Error: {temp.error.strip()}")
            print()
            temp = temp.next

    def print_commands_forward(self):
        temp = self.head
        # Traverse through the list and print each command in forward order
        while temp:
            print(temp.command, end=' <-> ' if temp.next else '')
            temp = temp.next
        print()

    def print_commands_backward(self):
        temp = self.head
        # Traverse to the end of the list
        while temp and temp.next:
            temp = temp.next
        # Traverse backward through the list and print each command
        while temp:
            print(temp.command, end=' <-> ' if temp.prev else '')
            temp = temp.prev
        print()

# Usage
cmd_list = CommandList()
cmd_list.add_command("echo 'Hello World'")
cmd_list.add_command("ls -l")
cmd_list.add_command("invalid_command")  # This will simulate a failed command
cmd_list.add_command("pwd")

print("Commands in order (Forward):")
cmd_list.print_commands_forward()

print("\nExecuting commands...")
cmd_list.execute_commands()

print("\nCommands status:")
cmd_list.print_commands_status()

print("\nCommands in order (Backward):")
cmd_list.print_commands_backward()
