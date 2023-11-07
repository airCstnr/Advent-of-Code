# 8.1

import sys
import re

if len(sys.argv) != 2:
    print("usage : python 8.1 input_file")
    exit()

with open(sys.argv[1], 'r') as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]

accumulator = 0
instructions = []
prog_counter = 0
prog_list = []

for line in lines:
    match = re.match(r"(\w{3}) (\+|\-)(\d+)", line)
    instructions.append(match.group(1, 2, 3))

while prog_counter not in prog_list:
    prog_list.append(prog_counter)
    ins, sign, val = instructions[prog_counter]
    if ins == 'nop':
        prog_counter += 1
    if ins == 'acc':
        if sign == '+':
            accumulator += int(val)
        else:
            accumulator -= int(val)
        prog_counter += 1
    if ins == 'jmp':
        if sign == '+':
            prog_counter += int(val)
        else:
            prog_counter -= int(val)


print('accumulator :', accumulator)
