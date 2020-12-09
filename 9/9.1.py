# 9.1

import sys

if len(sys.argv) != 2:
    print("usage : python 9.1 input_file")
    exit()

with open(sys.argv[1], 'r') as f:
    lines = f.readlines()

lines = [int(line.strip()) for line in lines]

first_number = 0
available_numbers = []

def check_number(number):
    """
    check if number is sum of two available numbers
    """
    global available_numbers
    for i, n1 in enumerate(available_numbers):
        for j, n2 in enumerate(available_numbers[i:]):
            if n1 + n2 == number:
                return True
    return False


for index, line in enumerate(lines):
    # store preamble number
    available_numbers.append(line)
    if index >= 25:
        # check number
        if check_number(line):
            available_numbers.pop(0)
        else:
            first_number = line
            break


print('first number :', first_number)
