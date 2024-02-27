import sys

# Created a dictionary to store log entries by IP address
logEntries = {}

for line in sys.stdin:
    line = line.strip()
    ipAddress, logEntry = line.split('\t', 1)
# Check if IP address is already in the dictionary and if not add it with empty list
    if ipAddress not in logEntries:
        logEntries[ipAddress] = []
# Adding log entry to list with corresponding IP Address
    logEntries[ipAddress].append(logEntry)
sortedIps = sorted(logEntries.keys())
# Iterating through IP Address and printing the IP Address and their Log Entries
for ipAddress in sortedIps:
    for logEntry in logEntries[ipAddress]:
        print(f"{ipAddress} {logEntry}")
        print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

