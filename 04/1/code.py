import time
start_time = time.time()
#open the file and parse it into a list of strings on newlines
text_file = open("input.txt", "r")
lines = text_file.read().split('\n\n')

count = 0
for i in range(0, len(lines)):
    lines[i] = lines[i].replace('\n', ' ')
    lines[i] = lines[i].split(' ')

lines[len(lines)-1].pop(len(lines[len(lines)-1])-1)
for i in range(0, len(lines)):
    j = 0
    while j < len(lines[i]):
        if(lines[i][j].find('cid') > -1):
            lines[i].pop(j)
            j += 1
        j += 1
    if(len(lines[i]) == 7):
        count += 1

print(count)
print("--- %s seconds ---" % (time.time() - start_time))
