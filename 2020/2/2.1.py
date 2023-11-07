# 2.1

number_of_valid_passwd = 0

with open('input.txt', 'r') as f:
    lines = f.readlines()

for l in lines:
    rule, letter, passwd = l.split(' ')
    letter = letter[0]
    min, max = rule.split('-')
    count=0
    for x in passwd.strip():
        if x == letter:
            count+=1
    if int(min) <= count <= int(max): 
        number_of_valid_passwd+=1

print('number_of_valid_passwd :', number_of_valid_passwd)