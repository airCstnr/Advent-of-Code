# 12.2

import sys

if len(sys.argv) != 2:
    print("usage : python 12.2 input_file")
    exit()

with open(sys.argv[1], 'r') as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]


#           N  E        
position = [0, 0]
waypoint = [1, 10]


for line in lines:
    action = line[0]
    value = int(line[1:])

    if action == 'N':
        waypoint[0] += value
    if action == 'S':
        waypoint[0] -= value
    if action == 'E':
        waypoint[1] += value
    if action == 'W':
        waypoint[1] -= value

    if action == 'L':
        tmp = waypoint.copy()
        if value == 90:
            waypoint[0] = tmp[1]
            waypoint[1] = -tmp[0]
        if value == 180:
            waypoint[0] = -tmp[0]
            waypoint[1] = -tmp[1]
        if value == 270:
            waypoint[0] = -tmp[1]
            waypoint[1] = tmp[0]
    if action == 'R':
        tmp = waypoint.copy()
        if value == 90:
            waypoint[0] = -tmp[1]
            waypoint[1] = tmp[0]
        if value == 180:
            waypoint[0] = -tmp[0]
            waypoint[1] = -tmp[1]
        if value == 270:
            waypoint[0] = tmp[1]
            waypoint[1] = -tmp[0]
    
    if action == 'F':
        position[0] += waypoint[0] * value
        position[1] += waypoint[1] * value


distance = abs(position[0]) + abs(position[1])
print("Manhattan distance :", distance)
