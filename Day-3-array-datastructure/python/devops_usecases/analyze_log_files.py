# List of log files from multiple servers
log_files = ["./logs/access.log", "./logs/error.log"]

# Function to analyze logs
def analyze_logs(log_file):
    error_patterns = {}
    with open(log_file, "r") as file:
        for line in file:
            if "error" in line.lower():
                error_type = line.split(":")[0]
                if error_type not in error_patterns:
                    error_patterns[error_type] = 0
                error_patterns[error_type] += 1
    return error_patterns

# Analyze logs and aggregate results
aggregated_errors = {}
for log_file in log_files:
    errors = analyze_logs(log_file)
    for error_type, count in errors.items():
        if error_type not in aggregated_errors:
            aggregated_errors[error_type] = 0
        aggregated_errors[error_type] += count

# Print aggregated error patterns
print("Aggregated error patterns:")
for error_type, count in aggregated_errors.items():
    print(f"{error_type}: {count}")
