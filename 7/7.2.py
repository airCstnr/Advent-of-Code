# 7.2

import sys
import re

if len(sys.argv) != 2:
    print("usage : python 7.2 input_file")
    exit()

with open(sys.argv[1], 'r') as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]
bags = {}

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
def required_inside_bags(color):
    """
    Recursive search for bags contained inside colored bag
    """
    global bags

    if len(bags[color]) == 0:
        # empty bag, requires 0
        return 0

    # search bags contained directly inside colored bag
    required = 0
    for bag in bags[color]:
        # 'count' times bag + 'count' times required bags inside bag
        req = required_inside_bags(bag[1])
        required += int(bag[0]) + (int(bag[0]) * req)
    return required


for line in lines:
    container, contained = line.split(' bags contain ')
    bags[container] = []
    match = re.findall(r"(\d) (\w+ \w+)", contained)
    for count, color in match:
        bags[container].append((count, color))


print('required bags :', required_inside_bags('shiny gold'))
