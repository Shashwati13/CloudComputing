import re
import sys

# Regex given to extract IP and hour in the Assignment.
pattern = re.compile(r'(\d+\.\d+\.\d+\.\d+).*?(\d{4}:\d{2}):\d{2}')

for line in sys.stdin:
    patternFound = pattern.search(line)
    if patternFound:
        ip, hour = patternFound.groups()
        print(f'Hour: {hour}, IP: {ip}, 1')

