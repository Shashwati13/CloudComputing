#!/usr/bin/env python

import sys

currentWord = None
currentCount = 0

for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t', 1)

    try:
        count = int(count)
    except ValueError:                                            
            continue

    if currentWord == word:
        currentCount += count
    else:
        if currentWord:
            print(f'{currentWord}\t{currentCount}')
            print("-------------------------------")
        currentWord = word
        currentCount = count
if currentWord:
    print(f'{currentWord}\t{currentCount}')

