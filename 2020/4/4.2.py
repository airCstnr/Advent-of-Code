# 4.2

import sys
import re

number_of_valid_passport = 0

if len(sys.argv) != 2:
    print("usage : python 4.2 input_file")
    exit()

with open(sys.argv[1], 'r') as f:
    lines = f.readlines()

required_fields = {
    "byr" : "Birth Year",
    "iyr" : "Issue Year",
    "eyr" : "Expiration Year",
    "hgt" : "Height",
    "hcl" : "Hair Color",
    "ecl" : "Eye Color",
    "pid" : "Passport ID",
    #"cid" : "Country ID"
}

def check_byr(byr):
    """
    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    """
    if len(byr) != 4:
        raise Exception("byr ({}): incorrect length ({}), expected 4".format(byr, len(byr)))
    if not byr.isnumeric():
        raise Exception("byr ({}): incorrect type, expected digits only".format(byr))
    if 1920 <= int(byr) <= 2002:
        pass
    else:
        raise Exception("byr ({}): value ourside bounds, expected 1920 <= byr <= 2002".format(byr))

def check_iyr(iyr):
    """
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    """
    if len(iyr) != 4:
        raise Exception("iyr ({}): incorrect length ({}), expected 4".format(iyr, len(iyr)))
    if not iyr.isnumeric():
        raise Exception("iyr ({}): incorrect type, expected digits only".format(iyr))
    if 2010 <= int(iyr) <= 2020:
        pass
    else:
        raise Exception("iyr ({}): value ourside bounds, expected 2010 <= iyr <= 2020".format(iyr))

def check_eyr(eyr):
    """
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    """
    if len(eyr) != 4:
        raise Exception("eyr ({}): incorrect length ({}), expected 4".format(eyr, len(eyr)))
    if not eyr.isnumeric():
        raise Exception("eyr ({}): incorrect type, expected digits only".format(eyr))
    if 2020 <= int(eyr) <= 2030:
        pass
    else:
        raise Exception("eyr ({}): value ourside bounds, expected 2020 <= eyr <= 2030".format(eyr))

def check_hgt(hgt):
    """
    hgt (Height) - a number followed by either cm or in:
    If cm, the number must be at least 150 and at most 193.
    If in, the number must be at least 59 and at most 76.
    """
    re.DEBUG
    match = re.match(r"^(\d+)(cm|in)$", hgt)
    if not match:
        raise Exception("hgt ({}): incorrect format ".format(hgt))
    value, unit = match.group(1, 2)
    if unit == "cm" and not (150 <= int(value) <= 193):
        raise Exception("hgt ({}): value ourside bounds, expected 150 <= hgt <= 193".format(value))
    if unit == "in" and not (59 <= int(value) <= 76):
        raise Exception("hgt ({}): value ourside bounds, expected 59 <= hgt <= 76".format(value))

def check_hcl(hcl):
    """
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    """
    re.DEBUG
    match = re.match(r"^#[0-9a-f]{6}$", hcl)
    if not match:
        raise Exception("hcl ({}): incorrect format ".format(hcl))

def check_ecl(ecl):
    """
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    """
    if ecl not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        raise Exception("ecl ({}) : incorrect value".format(ecl))

def check_pid(pid):
    """
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    """
    re.DEBUG
    match = re.match(r"^\d{9}$", pid)
    if not match:
        raise Exception("pid ({}): incorrect format".format(pid))

"""
cid (Country ID) - ignored, missing or not.
"""


def check_passport(pairs):
    fields = {}
    for pair in pairs:
        key, value = pair.split(':')
        fields[key] = value
    for req in required_fields:
        if req not in fields:
            raise Exception (req, "not in fields")
        # call check function
        #print("checking {} with {}...".format(required_fields[req], fields[req]), end='')
        globals()['check_'+req](fields[req])
        #print(" OK")
    #print("PASSPORT OK")



lines = [line.strip() for line in lines]
lines += [''] # append last line to process latest passeport

pairs = []

for line in lines:
    if line == '':
        try:
            check_passport(pairs)
            number_of_valid_passport += 1
        except Exception as e:
            #print(e)
            pass
        pairs = []
        #print()
        continue
    else:
        pairs += line.split(' ')


print('number of valid passports :', number_of_valid_passport)
