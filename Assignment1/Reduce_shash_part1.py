import sys
from collections import defaultdict

# To store hourly stats of IP address and their count
hourlyStats = defaultdict(lambda: defaultdict(int))

for line in sys.stdin:
    line = line.strip()
    hour, ip, count = line.split(',')
# Update the IP address with count of occurrences for specific hour
    hourlyStats[hour][ip] += int(count)

for hour, stats in hourlyStats.items():
    hourParts = hour.split(':')
    extractedHour = hourParts[2]
# Sorting in descending according the count and taking top 3 IP addresses 
    topIPs = sorted(stats.items(), key=lambda x: x[1], reverse=True)[:3]
# Printing top IP adresses, count and Hour
    for ip, count in topIPs:
        print("-------------------------------------------------------")
        print(f"TOTAL COUNT: {count}, {ip}, Hour: {extractedHour}:00")
print("-------------------------------------------------------")
