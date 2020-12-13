# 12.1

import sys

if len(sys.argv) != 2:
    print("usage : python 12.1 input_file")
    exit()

with open(sys.argv[1], 'r') as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]

#           N  E
position = [0, 0]
orientation = 0 # E

for line in lines:
    action = line[0]
    value = int(line[1:])

    if action == 'N':
        position[0] -= value
    if action == 'S':
        position[0] += value
    if action == 'E':
        position[1] += value
    if action == 'W':
        position[1] -= value

    if action == 'L':
        orientation -= value
    if action == 'R':
        orientation += value

    if action == 'F':
        # keep orientation between 0 and 360
        _, orientation = divmod(orientation, 360)
        if orientation == 270 : # N
            position[0] -= value
        elif orientation == 90: # S
            position[0] += value
        elif orientation == 0: # E
            position[1] += value
        elif orientation == 180: # W
            position[1] -= value
        else:
            raise Exception('Unexpected orientation')

distance = abs(position[0]) + abs(position[1])
print("Manhattan distance :", distance)