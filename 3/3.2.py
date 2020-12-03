# 3.2

total_number_of_trees = 1

with open('input.txt', 'r') as f:
    lines = f.readlines()

slopes = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
]

for slope in slopes:
    print()
    print('slope', slope)
    print()

    number_of_trees = 0
    right = 0
    down = 0

    for line in lines[slope[1]::slope[1]]:
        line = line.strip()
        right += slope[0]
        right %= len(line)
        
        print(line[:right], end='')
        if line[right] == '#':
            print('X', end='')
            number_of_trees+=1
        else:
            print('O', end='')
            pass
        print(line[right+1:])

    print('number of trees encountered: ', number_of_trees)
    print('down: ', down)
    total_number_of_trees *= number_of_trees


print('total number of trees encountered (multiplied): ', total_number_of_trees)