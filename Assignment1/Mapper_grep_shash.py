import sys
import re
import os

# Check if the 'search_pattern' environment variable is set
search_pattern = os.environ.get('search_pattern')
if not search_pattern:
    print("The 'search_pattern' environment variable is not defined")
    sys.exit(1)
patternFound = re.compile(search_pattern)
for line in sys.stdin:
    line = line.strip()
    if patternFound.search(line):
        print(line)
