# 7.1

import sys
import re

if len(sys.argv) != 2:
    print("usage : python 7.1 input_file")
    exit()

with open(sys.argv[1], 'r') as f:
    lines = f.readlines()

bags = {}


def search_bag_containers(color):
    """
    Recursive search for bags containing colored bag
    """
    global bags

    # search bags containing directly colored bag
    containers = set()
    for bag in bags:
        if color in bags[bag]:
            containers.add(bag)

    # search bags containing parent bags, recursively
    parent_containers = set()
    for bag in containers:
        parent_containers |= search_bag_containers(bag)
    
    # take intersection of containg bags and parent bags
    containers |= parent_containers

    return containers


lines = [line.strip() for line in lines]


for line in lines:
    container, contained = line.split(' bags contain ')
    bags[container] = []
    match = re.findall(r"(\d) (\w+ \w+)", contained)
    for count, color in match:
        bags[container].append(color)


containers = search_bag_containers('shiny gold')
sum_of_bags = len(containers)

print('sum of bags :', sum_of_bags)
