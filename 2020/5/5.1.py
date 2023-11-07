# 5.1

import sys
import math

if len(sys.argv) != 2:
    print("usage : python 5.1 input_file")
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


for line in lines:
    #print(line)
    rmin, rmax = 0, 127
    cmin, cmax = 0, 7
    for char in line:
        #print(char)
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
print('highest seat id :', highest_seat_id)
