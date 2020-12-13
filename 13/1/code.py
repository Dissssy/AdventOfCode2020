import time
start_time = time.time()
#open the file and parse it into a list of strings on newlines
text_file = open("input.txt", "r")
lines = text_file.read().split('\n')

#every input text file has an empty newline at the end, delete it
lines.pop(-1)

busid = lines[1].split(",")
i = 0
timestamp = int(lines[0])
while i < len(busid):
    if(busid[i] == "x"):
        busid.pop(i)
        i -= 1
    else:
        busid[i] = int(busid[i])
    i += 1

short = 0
timeuntil = max(busid)
for i in range(0, len(busid)):
    if busid[i] - (timestamp % busid[i]) <= timeuntil:
        short = busid[i]
        timeuntil = busid[i] - (timestamp % busid[i])

print(short * timeuntil)

print("--- %s seconds ---" % (time.time() - start_time))

