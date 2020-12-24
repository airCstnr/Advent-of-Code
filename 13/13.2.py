# 13.2

import sys

if len(sys.argv) != 2:
    print("usage : python 13.2 input_file")
    exit()

with open(sys.argv[1], 'r') as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]

bus_lines = lines[1].split(',')

t0 = 0
short_list = []


def search_t(index, step):
    """
    Search t that match constraint with others
    """
    global bus_lines
    global t0

    print('--', index, step)

    # stop condition
    if index >= len(bus_lines):
        print("end")
        return True

    line = bus_lines[index]

    # skip
    if line == 'x':
        print("skip x")
        return search_t(index+1, step)

    line = int(line)
    stop = False

    while not stop:
        _, offset = divmod(t0, line)
        #print((line - offset) % line)
        if (line - offset) % line == index:
            stop = search_t(index+1, step*line)
            print(t0, stop)
            #exit()
        else:
            t0 += step*line
            #stop = True
            print(t0)

    print(t0)
    return True



search_t(0, 1)
