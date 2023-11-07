# 9.2

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
encryption_weakness_list = []

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


def search_for_encryption_weakness(number):
    """
    Build encryption weakness list using lines
    """
    global lines
    global encryption_weakness_list
    
    # initialize list with 2 first numbers
    encryption_weakness_list = lines[:2]

    index = 0
    while sum(encryption_weakness_list) != number:
        if sum(encryption_weakness_list) < number:
            # add new available number
            encryption_weakness_list.append(lines[index])
            index += 1
        else:
            # remove first number ONLY if list contains more than 2 elements
            if len(encryption_weakness_list) > 2:
                encryption_weakness_list.pop(0)



for index, line in enumerate(lines):
    # store preamble number
    available_numbers.append(line)
    if index >= preamble_length:
        # check number
        if check_number(line):
            available_numbers.pop(0)
        else:
            first_number = line
            # search for encryption weakness
            search_for_encryption_weakness(line)
            break


#print('encryption weakness list :', encryption_weakness_list)

smallest = min(encryption_weakness_list, default='EMPTY')
largest  = max(encryption_weakness_list, default='EMPTY')
summ     = smallest + largest

print('encryption weakness smallest :', smallest)
print('encryption weakness largest  :', largest)
print('encryption weakness sum  :', summ)
