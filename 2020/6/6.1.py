# 6.1

import sys

if len(sys.argv) != 2:
    print("usage : python 6.1 input_file")
    exit()

with open(sys.argv[1], 'r') as f:
    lines = f.readlines()


sum_of_counts = 0

lines = [line.strip() for line in lines]
lines += [''] # append last line to process latest group

questions_answered = set()

for line in lines:
    #print(line)
    if line == '':
        #print(questions_answered)
        sum_of_counts += len(questions_answered)
        # reset variable
        questions_answered = set()
        continue
    else:
        for l in line:
            questions_answered.add(l)

print('sum of counts :', sum_of_counts)
