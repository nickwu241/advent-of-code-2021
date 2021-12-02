#!/usr/bin/env python
with open('input') as f:
    depths = [int(line) for line in f]

# Puzzle 1
import sys

number_of_increases = 0
previous = sys.maxint
for depth in depths:
    if depth > previous:
        number_of_increases += 1
    previous = depth

print(number_of_increases)

# Puzzle 2
number_of_increases = 0
previous = sys.maxint
for i in range(len(depths) - 2):
    sum_of_window = sum(depths[i:i+3])
    if sum_of_window > previous:
        number_of_increases += 1
    previous = sum_of_window
print(number_of_increases)
