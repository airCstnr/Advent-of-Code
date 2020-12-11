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


#@memoize
def count_number_of_distinct_ways(index):
    """
    Count number of distinct ways from one adapter
    """
    global lines
    number_of_distinct_ways = 0
    print(index, ":", lines[index:])

    if lines[index]

    step = 1

    while index+step<len(lines):
        number_of_distinct_ways += count_number_of_distinct_ways(index+step)
        step += 1
    return number_of_distinct_ways

"""
    for step in range(1, 4):
        print(lines[next_index])
    return number_of_distinct_ways
        if index+next_index < len(lines):
            diff = lines[index+next_index] - lines[index]
            if diff in range(1, 4):
                number_of_distinct_ways += count_number_of_distinct_ways(index+next_index)
            else:
                # not a valuable
                break
        else:
            # can't continue further
            number_of_distinct_ways += 1
            break

    print("end >", index, number_of_distinct_ways)
    return number_of_distinct_ways
"""

number_of_distinct_ways = count_number_of_distinct_ways(0)

print('number of distinct ways :', number_of_distinct_ways)
