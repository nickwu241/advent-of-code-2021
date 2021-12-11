#!/usr/bin/env python3
with open('input') as f:
    movements = [line.split() for line in f]

# Puzzle 1
depth = 0
horizontal = 0
for direction, steps in movements:
    steps = int(steps)
    if direction == 'forward':
        horizontal += steps
    elif direction == 'up':
        depth -= steps
    elif direction == 'down':
        depth += steps
    else:
        raise AssertionError(f'Unknown direction: {direction}')

answer = depth * horizontal
print(answer)

# Puzzle 2
aim = 0
depth = 0
horizontal = 0
for direction, steps in movements:
    steps = int(steps)
    if direction == 'forward':
        horizontal += steps
        depth += aim * steps
    elif direction == 'up':
        aim -= steps
    elif direction == 'down':
        aim += steps
    else:
        raise AssertionError(f'Unknown direction: {direction}')

answer = depth * horizontal
print(answer)