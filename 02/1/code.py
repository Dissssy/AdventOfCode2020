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
#parse that string into two ints, the min and max, and a string, the letter for the rule
#return those three variables as a list
def parserule(rule):
    tmp, letter = rule.split(' ')
    min, max = tmp.split('-')
    return [int(min), int(max), letter]

#for every string in list lines
#split that string into two strings, between the rule and the password
#store each of those in the lists rule, and password
#also delete a rogue space in the password list because niceness
for i in range(0, len(lines)):
    rule[i], password[i] = lines[i].split(':')
    password[i] = password[i].replace(' ', '')

#for every string in list password
#parse the corresponding rule into its constituent parts, the min, max, and letter
#if the number of those letters in the current password string is within the bounds set by the rule
#add one to the count
for i in range(0, len(password)):
    thisrule = parserule(rule[i])
    if(thisrule[0] <= password[i].count(thisrule[2]) <= thisrule[1]):
        count += 1

#print the final count
print(count)
