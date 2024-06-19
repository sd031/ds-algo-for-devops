# List of server IP addresses
servers = ["192.168.1.1", "192.168.1.2", "192.168.1.3"]

# Function to get the next server in round-robin fashion
def get_next_server(current_index):
    return (current_index + 1) % len(servers)

# Example usage
current_index = 0
for _ in range(5):
    current_index = get_next_server(current_index)
    print(servers[current_index])
# Output: 192.168.1.2, 192.168.1.3, 192.168.1.1, 192.168.1.2, 192.168.1.3
