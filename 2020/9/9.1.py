# 9.1

import sys

if len(sys.argv) != 3:
    print("usage : python 9.2 input_file preamble_length")
    exit()

with open(sys.argv[1], 'r') as f:
    lines = f.readlines()

lines = [int(line.strip()) for line in lines]

preamble_length = int(sys.argv[2])
first_number = 0
available_numbers = []

def check_number(number):
    """
    check if number is sum of two available numbers
    """
    global available_numbers
    for i, n1 in enumerate(available_numbers):
        for n2 in available_numbers[i:]:
            if n1 + n2 == number:
                return True
    return False


for index, line in enumerate(lines):
    # store preamble number
    available_numbers.append(line)
    if index >= preamble_length:
        # check number
        if check_number(line):
            available_numbers.pop(0)
        else:
            first_number = line
            break


print('first number :', first_number)
