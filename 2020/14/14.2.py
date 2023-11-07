# 14.2

import sys

if len(sys.argv) != 2:
    print("usage : python 14.2 input_file")
    exit()

with open(sys.argv[1], 'r') as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]

mask = ['X' for i in range(36)]
mem = {}

def apply(before, after, value):
    """ Assign value to all given adresses

    Adresses is full if after is empty
    Otherwise, call apply with 1 more bit
    """
    #print(before, after, value)
    if len(after) == 0:
        global mem
        addr = int('0b'+"".join(before), base=2)
        #print("ready", addr, value)
        mem[addr] = value
        return
    else:
        #print("build addresses")
        if after[0] == 'X':
            before.append('0')
            apply(before, after[1:], value)
            before.pop()
            before.append('1')
            apply(before, after[1:], value)
            before.pop()
        else:
            before.append(after[0])
            apply(before, after[1:], value)
            before.pop()


for line in lines:
    left, right = line.split('=')
    left = left.strip()
    right = right.strip()
    if left == "mask":
        mask = [val for val in right]
    else:
        # get mem key between [ and ]
        address = left[4:-1]
        # convert address value to 36-bits binary
        value = bin(int(address))[2:].zfill(36)
        # compute result using mask
        result = ['0' for i in range(36)]
        for i, mask_value in enumerate(mask):
            if mask_value == '0':
                result[i] = value[i]
            elif mask_value == '1':
                result[i] = '1'
            else:
                result[i] = mask_value
        # store value in mem at result using binary-to-int conversion
        apply([], result, int(right))


sum = 0
for value in mem.values():
    sum += value

print("sum :", sum)