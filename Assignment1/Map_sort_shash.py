import sys


for line in sys.stdin:
    line = line.strip()
    words = line.split()
    if words:
        IPAddress, *rest = words
        print(f"{IPAddress}\t{' '.join(rest)}")
