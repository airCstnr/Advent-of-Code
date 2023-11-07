# 6.2

import sys

if len(sys.argv) != 2:
    print("usage : python 6.2 input_file")
    exit()

with open(sys.argv[1], 'r') as f:
    lines = f.readlines()


sum_of_counts = 0

lines = [line.strip() for line in lines]
lines += [''] # append last line to process latest group

common_answers = set()
first = True

for line in lines:
    #print(line)
    if line == '':
        #print(common_answers)
        sum_of_counts += len(common_answers)
        # reset variable
        common_answers = set()
        first = True
        continue
    else:
        if first:
            common_answers.update(line)
            first = False
        else:
            # use intersection property of set
            common_answers &= set(line)

print('sum of counts :', sum_of_counts)
