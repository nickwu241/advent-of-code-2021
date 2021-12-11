#!/usr/bin/env python3
with open('input') as f:
    n_bits = len(f.readline().strip())
    # print(n_bits)
    f.seek(0)
    report = [int(line, 2) for line in f]

# Puzzle 1

# by position, reverse order
zero_bit_counts = [0] * n_bits
one_bit_counts = [0] * n_bits
for value in report:
    # print(f'{{:0{n_bits}b}}'.format(value))
    for shift in range(n_bits):
        bit_is_one = bool(value & (1 << shift))
        if bit_is_one:
            one_bit_counts[shift] += 1
        else:
            zero_bit_counts[shift] += 1

# print(one_bit_counts)
# print(zero_bit_counts)
gamma = 0
epsilon = 0
for shift, (n_zeros, n_ones) in enumerate(zip(zero_bit_counts, one_bit_counts)):
    if n_ones > n_zeros:
        gamma += 1 << shift
    else:
        epsilon += 1 << shift

answer = gamma * epsilon
print(answer)

# Puzzle 2
def get_most_and_least_common_bit(values, shift):
    n_ones = n_zeros = 0
    for value in values:
        bit_value = (value >> shift & 1)
        n_ones += int(bit_value == 1)
        n_zeros += int(bit_value == 0)
    return int(n_ones >= n_zeros), int(n_ones < n_zeros)

def discard_if_not_equal(values, shift, bit):
    pos = 0
    for _ in range(len(values)):
        if len(values) <= 1:
            return
        if (values[pos] >> shift) % 2 != bit:
            values.pop(pos)
        else:
            pos += 1

o2 = list(report)
co2 = list(report)
for shift in range(n_bits-1, -1, -1):
    most_common_bit, _ = get_most_and_least_common_bit(o2, shift)
    discard_if_not_equal(o2, shift, most_common_bit)
    _ , least_common_bit = get_most_and_least_common_bit(co2, shift)
    discard_if_not_equal(co2, shift, least_common_bit)

# print(o2, co2)
answer = o2[0] * co2[0]
print(answer)
