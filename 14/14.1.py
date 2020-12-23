# 14.1

import sys

if len(sys.argv) != 2:
    print("usage : python 14.1 input_file")
    exit()

with open(sys.argv[1], 'r') as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]

mask = ['X' for i in range(36)]
mem = {}

for line in lines:
    left, right = line.split('=')
    left = left.strip()
    right = right.strip()
    if left == "mask":
        mask = [val for val in right]
    else:
        # get mem key between [ and ]
        key = left[4:-1]
        # convert right value to 36-bits binary
        value = bin(int(right))[2:].zfill(36)
        # compute result using mask
        result = ['0' for i in range(36)]
        for i, mask_value in enumerate(mask):
            if mask_value == 'X':
                result[i] = value[i]
            else:
                result[i] = mask_value
        # store result in mem using binary-to-int conversion
        mem[key] = int('0b'+"".join(result), base=2)

sum = 0
for value in mem.values():
    sum += value

print("sum :", sum)