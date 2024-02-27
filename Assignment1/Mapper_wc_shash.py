#!/usr/bin/env python

import sys
import re

# Initialize a dictionary to store word counts
wordCount = {}

for line in sys.stdin:
    line = line.strip()
    words = line.split()
    words = re.findall(r'\b\w+\b|\.\w+\b', line)
    for w in words:
# Increment the word count in the dictionary
        wordCount[w] = wordCount.get(w, 0) + 1
# Output word counts to STDOUT
for w, c in wordCount.items():
     print(f'{w}\t{c}')

