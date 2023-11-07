# 8.2

import sys
import re

if len(sys.argv) != 2:
    print("usage : python 8.2 input_file")
    exit()

with open(sys.argv[1], 'r') as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]

instructions = []

for line in lines:
    match = re.match(r"(\w{3}) (\+|\-)(\d+)", line)
    instructions.append([match.group(1), match.group(2), match.group(3)])


def run_instructions():
    """
    Run instruction list.

    Returns true if terminated and accumulator value
    run_instructions() -> (terminated, accumulator)
    """
    global instructions

    accumulator = 0
    prog_counter = 0
    prog_list = []

    while prog_counter not in prog_list:
        # terminated
        if prog_counter == len(instructions):
            return (True, accumulator)
        
        # store current instruction index
        prog_list.append(prog_counter)

        # get instruction
        ins, sign, val = instructions[prog_counter]
        
        # execute instruction
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

    return (False, accumulator)


def search_corrupted_instruction():
    """
    Change each 'jmp' to 'nop' (and vice versa) to find corrupted instruction
    """
    global instructions

    for i in range(len(instructions)):
        (ins, _, _) = instructions[i]
        if ins == 'jmp':
            instructions[i][0] = 'nop'
            terminated, accumulator = run_instructions()
            if terminated:
                return accumulator
            instructions[i][0] = 'jmp'
        if ins == 'nop':
            instructions[i][0] = 'jmp'
            terminated, accumulator = run_instructions()
            if terminated:
                return accumulator
            instructions[i][0] = 'nop'


accumulator = search_corrupted_instruction()
print('accumulator :', accumulator)
