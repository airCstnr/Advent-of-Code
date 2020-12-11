# 10.1

import sys

if len(sys.argv) != 2:
    print("usage : python 10.1 input_file")
    exit()

with open(sys.argv[1], 'r') as f:
    lines = f.readlines()

lines = [int(line.strip()) for line in lines]
lines = sorted(lines)

_1_jolt_diff = 0
_3_jolt_diff = 0

prev = 0

for line in lines:
    diff = line - prev
    if diff == 1:
        _1_jolt_diff += 1
    elif diff == 3:
        _3_jolt_diff += 1
    else:
        raise Exception("diff between {} and {} is neither 1 or 3".format(prev, line))
    prev = line

# don't forget that device's built-in adapter is always 3 higher than the highest adapter
_3_jolt_diff += 1

mult = _1_jolt_diff * _3_jolt_diff

print('1-jolt differences :', _1_jolt_diff)
print('3-jolt differences  :', _3_jolt_diff)
print('multiplied :', mult)
