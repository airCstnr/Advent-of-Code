# 3.1

number_of_trees = 0

with open('input.txt', 'r') as f:
    lines = f.readlines()

right = 0
down = 0

for line in lines[1:]:
    line = line.strip()
    right += 3
    right %= len(line)
    
    #print(line[:right], end='')
    if line[right] == '#':
        #print('X', end='')
        number_of_trees+=1
    #else:
        #print('O', end='')
    #print(line[right+1:])

print('number of trees encountered: ', number_of_trees)
