# List of server IP addresses
servers = ["192.168.1.1", "192.168.1.2", "192.168.1.3"]

# Accessing a server's IP address
print(servers[0])  # Output: 192.168.1.1

# Adding a new server
servers.append("192.168.1.4")
print(servers)  # Output: ['192.168.1.1', '192.168.1.2', '192.168.1.3', '192.168.1.4']

# Removing a server
servers.remove("192.168.1.2")
print(servers)  # Output: ['192.168.1.1', '192.168.1.3', '192.168.1.4']
