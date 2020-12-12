# 10.2

import sys

if len(sys.argv) != 2:
    print("usage : python 10.2 input_file")
    exit()

with open(sys.argv[1], 'r') as f:
    lines = f.readlines()

lines = [int(line.strip()) for line in lines]
lines = sorted(lines)

goal = max(lines) + 3
full_list = [0] + lines + [goal]


def memoize(f):
    """
    Memoize data to reduce memory usage
    """
    memo = {}
    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper


@memoize
def neighbors(index):
    """
    Returns neighbors for given index
    """
    global full_list
    candidates = []
    # candidate must be away of 3 steps maximum
    for add in range(1, 4):
        try:
            diff = full_list[index+add] - full_list[index]
            # candidate is already too far
            if diff > 3:
                break
            else:
                candidates.append(index+add)
        except:
            break
    return candidates


@memoize
def count_number_of_distinct_ways(index):
    """
    Count number of distinct ways are accessibles from given index
    """
    global lines
    if index == len(lines):
        # latest element in the list (must be reached)
        return 1

    # count number of distinct ways for each neighbour
    num_sequences = 0
    for position in neighbors(index):
        num_sequences += count_number_of_distinct_ways(position)
    return num_sequences


"""
print(full_list)
for index in range(len(full_list)):
    print(index, ':', neighbors(index))
"""

number_of_distinct_ways = count_number_of_distinct_ways(0)
print('number of distinct ways :', number_of_distinct_ways)
