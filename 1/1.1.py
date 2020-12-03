# 1.1

with open('input.txt', 'r') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    print("{} : {}".format(i, line.strip()))
    for j, x in enumerate(lines[i+1:]):
        summ = int(x.strip()) + int(line.strip())
        prod = int(x.strip()) * int(line.strip())
        if summ == 2020:
            print("  {} : x = {}\t {} + {} = {}".format(j, x.strip(), x.strip(), line.strip(), summ))
            print("  {} x {} = {}".format(x.strip(), line.strip(), prod))
            break
    else:
        continue  # only executed if the inner loop did NOT break
    break  # only executed if the inner loop DID break
