text_file = open("input.txt", "r")
lines = text_file.read().split('\n')

count = 0

lines.pop(-1)

rule = ['']*(len(lines))
password = ['']*(len(lines))

def parserule(rule):
    tmp, letter = rule.split(' ')
    min, max = tmp.split('-')
    return [int(min), int(max), letter]

for i in range(0, len(lines)):
    rule[i], password[i] = lines[i].split(':')
    password[i] = password[i].replace(' ', '')

for i in range(0, len(password)):
    thisrule = parserule(rule[i])
    if(thisrule[0] <= password[i].count(thisrule[2]) <= thisrule[1]):
        count += 1
        print("{} {} {} {}".format(thisrule[0], thisrule[1], thisrule[2], password[i]))

print(count)
