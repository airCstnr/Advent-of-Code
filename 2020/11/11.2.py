# 11.2

import sys
import copy

if len(sys.argv) != 2:
    print("usage : python 11.2 input_file")
    exit()

with open(sys.argv[1], 'r') as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]

seats = []
for line in lines:
    seats.append([seat for seat in line])

adjacent_indexes = [
    (-1, -1),   # NW
    (-1, 0),    # N
    (-1, +1),   # NE
    (0, -1),    # W
    (0, +1),    # E
    (+1, -1),   # SW
    (+1, 0),    # S
    (+1, +1),   # SE
]


def print_seats():
    global seats
    for row in seats:
        for seat in row:
            print(seat, end='')
        print()
    print()


def count_occupied_seats():
    global seats
    occupied = 0
    for row in seats:
        for seat in row:
            if seat == '#':
                occupied += 1
    return occupied


def do_one_step(seats):
    # copy seats, from nested lists
    new_seats = copy.deepcopy(seats)
    changed = False
    for i, row in enumerate(seats):
        for j, seat in enumerate(row):
            # skip floor
            if seat == '.':
                continue
            empty_neighbours = 0
            occupied_neighbours = 0
            for adj_i, adj_j in adjacent_indexes:
                for k in range(1, len(row)):
                    try:
                        i_k = adj_i * k
                        j_k = adj_j * k
                        if i+i_k >= 0 and j+j_k >= 0:
                            s = seats[i+i_k][j+j_k]
                            if s == 'L':
                                empty_neighbours += 1
                                break
                            if s == '#':
                                occupied_neighbours += 1
                                break
                        else:
                            break
                    except:
                        break
            if seat == 'L' and occupied_neighbours == 0:
                new_seats[i][j] = '#'
                changed = True
            if seat == '#' and occupied_neighbours >= 5:
                new_seats[i][j] = 'L'
                changed = True
    return changed, new_seats


print_seats()
changed = True
while changed:
    changed, new_seats = do_one_step(seats)
    seats = new_seats.copy()
    #print_seats()

print("number of occupied seats : ", count_occupied_seats())
