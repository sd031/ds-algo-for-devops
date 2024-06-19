# Sample log entries
logs = [
    "2024-06-18 12:00:00 - INFO - Server started",
    "2024-06-18 12:01:00 - ERROR - Failed to connect to database",
    "2024-06-18 12:02:00 - INFO - Request received"
]

# Analyzing log entries
error_logs = [log for log in logs if "ERROR" in log]
print(error_logs)  # Output: ['2024-06-18 12:01:00 - ERROR - Failed to connect to database']
