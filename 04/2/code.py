import re
#open the file and parse it into a list of strings on newlines
text_file = open("input.txt", "r")
lines = text_file.read().split('\n\n')

def check(thisline):
    for j in range(0, len(thisline)):
        try:
            thisline[j] = thisline[j].split(':')
            if(thisline[j][0] == 'byr'):
                if(1920 > int(thisline[j][1]) or int(thisline[j][1]) > 2002):
                    return False
            elif(thisline[j][0] == 'iyr'):
                if(2010 > int(thisline[j][1]) or int(thisline[j][1]) > 2020):
                    return False
            elif(thisline[j][0] == 'eyr'):
                if(2020 > int(thisline[j][1]) or int(thisline[j][1]) > 2030):
                    return False
            elif(thisline[j][0] == 'hgt'):
                if(thisline[j][1].find('cm') > -1):
                    if(150 > int(thisline[j][1].replace('cm', '')) or int(thisline[j][1].replace('cm', '')) > 193):
                        return False
                elif(thisline[j][1].find('in') > -1):
                    if(59 > int(thisline[j][1].replace('in', '')) or int(thisline[j][1].replace('in', '')) > 76):
                        return False
                else:
                    return False
            elif(thisline[j][0] == 'hcl'):
                if not(re.search(r'^#(?:[0-9a-fA-F]{1,2}){3}$', thisline[j][1])):
                    return False
            elif(thisline[j][0] == 'ecl'):
                if('amb blu brn gry grn hzl oth'.find(thisline[j][1]) == -1):
                    return False 
            elif(thisline[j][0] == 'pid'):
                if(len(thisline[j][1]) != 9):
                    return False
            else:
                return False
        except:
            return False
    return True

count = 0
for i in range(0, len(lines)):
    lines[i] = lines[i].replace('\n', ' ')
    lines[i] = lines[i].split(' ')

lines[len(lines)-1].pop(len(lines[len(lines)-1])-1)
i = 0
while i < len(lines):
    j = 0
    while j < len(lines[i]):
        if(lines[i][j].find('cid') > -1):
            lines[i].pop(j)
            j += 1
        j += 1
    if(len(lines[i]) == 7):
        pass
        #count += 1
    else:
        lines.pop(i)
        i -= 1
    i += 1

for i in range(0, len(lines)):
    if check(lines[i]):
        count += 1
        #print(True)
    else:
        pass
        #print(False)
    #print(lines[i])

print(count)

