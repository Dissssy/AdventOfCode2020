import time
start_time = time.time()
#open the file and parse it into a list of strings on newlines
text_file = open("input.txt", "r")
lines = text_file.read().split('\n')

#every input text file has an empty newline at the end, delete it
lines.pop(-1)

def isvalid(i):
    for j in range(i - 25, i):
        for l in range(j + 1, i):
            if(lines[j] + lines[l] == lines[i]):
                return True
    return False

for i in range(0, len(lines)):
    lines[i] = int(lines[i])

for i in range(25, len(lines)):
    if not isvalid(i):
        print(lines[i])
        break

print("--- %s seconds ---" % (time.time() - start_time))
