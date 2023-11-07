# 1.2

with open('input.txt', 'r') as f:
    lines = f.readlines()

for i, x in enumerate(lines):
    #print("{} : {}".format(i, x.strip()))
    for j, y in enumerate(lines[i+1:]):
        #print("  {} : {}".format(j, y.strip()))
        for k, z in enumerate(lines[j+1:]):
            #print("    {} : {}".format(k, z.strip()))
            summ = int(x.strip()) + int(y.strip()) + int(z.strip())
            prod = int(x.strip()) * int(y.strip()) * int(z.strip())
            if summ == 2020:
                print("\t{} + {} + {} = {}".format(x.strip(), y.strip(), z.strip(), summ))
                print("\t{} * {} * {} = {}".format(x.strip(), y.strip(), z.strip(), prod))
                break
        else:
            continue  # only executed if the inner loop did NOT break
        break  # only executed if the inner loop DID break
    else:
        continue  # only executed if the inner loop did NOT break
    break  # only executed if the inner loop DID break
