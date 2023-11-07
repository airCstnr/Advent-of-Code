# 13.1

import sys

if len(sys.argv) != 2:
    print("usage : python 13.1 input_file")
    exit()

with open(sys.argv[1], 'r') as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]

arrival_ts = int(lines[0])
bus_lines = lines[1].split(',')

earliest_bus = 0
minutes_wait = sys.maxsize

for line in bus_lines:
    if line == 'x':
        continue
    line = int(line)
    _, time_since_latest_bus = divmod(arrival_ts, line)
    wait_time = line - time_since_latest_bus
    if wait_time < minutes_wait:
        earliest_bus = line
        minutes_wait = wait_time


print('earliest_bus :', earliest_bus)
print('minutes_wait :', minutes_wait)

print('answer :', earliest_bus * minutes_wait)
