# 5.2

import sys
import math
import time

if len(sys.argv) != 2:
    print("usage : python 5.2 input_file")
    exit()

with open(sys.argv[1], 'r') as f:
    lines = f.readlines()


highest_seat_id = 0

lines = [line.strip() for line in lines]

plane = [['.' for i in range(8)] for j in range(127)]

def print_plane():
    """
    Bonus function
    """
    for i, row in enumerate(plane):
        print("{:03d}".format(i), end=': ')
        for j, seat in enumerate(row):
            if j == 4:
                print(' ', end='')
            print(seat, end='')
        print()


def search_seat():
    prev_prev_seat = '.'
    prev_seat = '.'
    seat_id = 0
    for i, row in enumerate(plane):
        for j, seat in enumerate(row):
            if prev_prev_seat == 'X' and prev_seat == '.' and seat == 'X':
                seat_id = i * 8 + j - 1 # previous seat (not current one!)
                break
            prev_prev_seat = prev_seat
            prev_seat = seat
        else:
            continue  # only executed if the inner loop did NOT break
        break  # only executed if the inner loop DID break
    return seat_id


for line in lines:
    rmin, rmax = 0, 127
    cmin, cmax = 0, 7
    for char in line:
        if char == 'F':
            rmax = math.floor((rmax-rmin)/2)+rmin
        if char == 'B':
            rmin = math.ceil((rmax-rmin)/2)+rmin
        if char == 'L':
            cmax = math.floor((cmax-cmin)/2)+cmin
        if char == 'R':
            cmin = math.ceil((cmax-cmin)/2)+cmin
        #print(rmin, rmax, cmin, cmax)
    assert(rmin == rmax)
    assert(cmin == cmax)
    seat_id = rmin * 8 + cmin
    #print(rmin, cmin, seat_id)
    if seat_id > highest_seat_id:
        highest_seat_id = seat_id
    plane[rmin][cmin] = 'X'


print_plane()
print('seat id :', search_seat())
