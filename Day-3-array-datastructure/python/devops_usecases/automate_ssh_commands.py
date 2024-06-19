import paramiko

# List of server IP addresses
servers = ["192.168.1.1", "192.168.1.2", "192.168.1.3"]

# SSH credentials
username = "admin"
password = "password"

# Command to run on each server
command = "uptime"

# Function to run SSH command
def run_ssh_command(server, command):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(server, username=username, password=password)
    stdin, stdout, stderr = ssh.exec_command(command)
    print(f"Output from {server}:")
    print(stdout.read().decode())
    ssh.close()

# Run command on each server
for server in servers:
    run_ssh_command(server, command)
