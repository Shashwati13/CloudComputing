import re
import sys
import os

# Extracting starting hour and ending hour from env variable time window
startHour, endHour = map(int, os.environ.get('timewindow').split("-"))
pattern = re.compile(r'(\d+\.\d+\.\d+\.\d+).*?(\d{4}:\d{2}):\d{2}')

for line in sys.stdin:
    patternFound = pattern.search(line)
    if patternFound:
        ip, hour = patternFound.groups()
        hourParts = hour.split(':')
        _, _, extractedHour = hour.partition(':')
# Extract the hour as integer value
        extractedHour = int(extractedHour)
# Checked if the extracted hour is withing starting and ending hour window
        if startHour <= extractedHour < endHour:
            print('Hour:', hour, ', IP:', ip, ', 1', sep='')
        else:
            continue
