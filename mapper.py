#!/usr/bin/env python
import sys

# Reading from stdin
for line in sys.stdin:
    # Remove leading/trailing whitespaces
    line = line.strip()
    
    # Split the line into words (assuming space-separated words)
    words = line.split()
    
    # Output each word with count 1
    for word in words:
        print(f"{word}\t1")
