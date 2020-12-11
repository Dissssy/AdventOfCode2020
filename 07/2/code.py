import time
start_time = time.time()
#open the file and parse it into a list of strings on newlines
text_file = open("input.txt", "r")
lines = text_file.read().split('\n')

#every input text file has an empty newline at the end, delete it
lines.pop(-1)

inbag = {}

def countin(bag):
    count = 1
    if bag in inbag:
        return inbag[bag]
    else:
        if len(lines[key[bag]][1]) == 0:
            return 1
        for i in range(0, len(lines[key[bag]][1])):
            count += int(lines[key[bag]][1][i][0]) * int(countin(lines[key[bag]][1][i][1]))
    inbag[bag] = count
    return count

for i in range(0, len(lines)):
    lines[i] = lines[i].split(" bags contain ")
    if lines[i][1] == "no other bags.":
        lines[i][1] = []
    else:
        lines[i][1] = lines[i][1].split(", ")
        for j in range(len(lines[i][1])):
            lines[i][1][j] = lines[i][1][j].split(' ', 1)
            for l in range(len(lines[i][1][j])):
                lines[i][1][j][l] = lines[i][1][j][l].replace(' bags', '').replace(' bag', '').replace('.', '')

key = {}

for i in range(0, len(lines)):
    key[lines[i][0]] = i

print(countin("shiny gold") - 1)
print("--- %s seconds ---" % (time.time() - start_time))
