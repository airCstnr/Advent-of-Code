# 2.2

number_of_valid_passwd = 0

with open('input.txt', 'r') as f:
    lines = f.readlines()

for e, l in enumerate(lines):
    rule, letter, passwd = l.split(' ')
    letter = letter[0]
    first, last = rule.split('-')
    count=0
    for i, x in enumerate(passwd.strip()):
        if (i+1 in [int(first), int(last)]) and x == letter:
            count+=1
    if 1 == count:
        number_of_valid_passwd+=1

print('number_of_valid_passwd :', number_of_valid_passwd)