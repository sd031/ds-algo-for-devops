import shutil

# List of directories to monitor
directories = ["/var/log", "/Users/Shared"]

# Disk usage threshold in bytes (e.g., 1GB)
threshold = 1 * 1024 * 1024 * 1024

# Function to check disk usage
def check_disk_usage(directory):
    total, used, free = shutil.disk_usage(directory)
    return used

# Monitor disk usage and alert if threshold is exceeded
for directory in directories:
    used = check_disk_usage(directory)
    if used > threshold:
        print(f"Alert: Disk usage in {directory} is above threshold! Used: {used} bytes")
    else:
        print(f"Disk usage in {directory} is under control. Used: {used} bytes")
