import time
start_time = time.time()
#open the file and parse it into a list of strings on newlines
text_file = open("input.txt", "r")
lines = text_file.read().split('\n')

#every input text file has an empty newline at the end, delete it
lines.pop(-1)

#initialize needed variables
count = 0
rule = ['']*(len(lines))
password = ['']*(len(lines))

#define the function parserule
#take a string formatted like the rules provided for the challenge
#parse that string into two ints, the posone and postwo, and a string, the letter for the rule
#return those three variables as a list
def parserule(rule):
    tmp, letter = rule.split(' ')
    posone, postwo = tmp.split('-')
    return [int(posone), int(postwo), letter]

#for every string in list lines
#split that string into two strings, between the rule and the password
#store each of those in the lists rule, and password
#also delete a rogue space in the password list because niceness
for i in range(0, len(lines)):
    rule[i], password[i] = lines[i].split(':')
    password[i] = password[i].replace(' ', '')

#for every strin in list password
#parse the corresponding rule into its constituent parts, posone, postwo, and letter
#check the character at posone against the letter
#check the character at potwo against the letter
#xor the result of those checks
#if the xor returns true, then add one to the count
for i in range(0, len(password)):
    thisrule = parserule(rule[i])
    if (password[i][thisrule[0] - 1] == thisrule[2]) ^ (password[i][thisrule[1] - 1] == thisrule[2]):
        count += 1

#print the final count
print(count)
print("--- %s seconds ---" % (time.time() - start_time))
