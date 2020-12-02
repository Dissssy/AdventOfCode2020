text_file = open("input.txt", "r")
lines = text_file.read().split('\n')

count = 0

lines.pop(-1)

rule = ['']*(len(lines))
password = ['']*(len(lines))

def parserule(rule):
    tmp, letter = rule.split(' ')
    posone, postwo = tmp.split('-')
    return [int(posone), int(postwo), letter]

for i in range(0, len(lines)):
    rule[i], password[i] = lines[i].split(':')
    password[i] = password[i].replace(' ', '')

for i in range(0, len(lines)):
    thisrule = parserule(rule[i])
    if (password[i][thisrule[0] - 1] == thisrule[2]) ^ (password[i][thisrule[1] - 1] == thisrule[2]):
        count += 1

print(count)
