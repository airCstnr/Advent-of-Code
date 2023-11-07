# 4.1

number_of_valid_passport = 0

with open('input.txt', 'r') as f:
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

lines = [line.strip() for line in lines]
lines += [''] # append last line to process latest passeport

pairs = []
fields = []

for line in lines:
    #print(line)
    if line == '':
        #print(pairs)
        for pair in pairs:
            key, value = pair.split(':')
            #print(key, value)
            fields.append(key)
        #print(fields)
        try:
            for req in required_fields:
                if req not in fields:
                    raise Exception (req, "not in fields")
            number_of_valid_passport += 1
        except Exception as e:
            #print(e)
            pass
        finally:
            # reset variables for next passport
            pairs = []
            fields = []
            continue
    else:
        pairs += line.split(' ')


print('number of valid passports: ', number_of_valid_passport)
