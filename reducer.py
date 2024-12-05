#!/usr/bin/env python
import sys
from collections import defaultdict

word_counts = defaultdict(int)

# Read from STDIN (input comes from mapper output)
for line in sys.stdin:
    word, count = line.strip().split('\t')
    word_counts[word] += int(count)

# Output final word counts to STDOUT
for word, count in word_counts.items():
    print(f"{word}\t{count}")
