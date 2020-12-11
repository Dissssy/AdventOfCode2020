import time
start_time = time.time()
from collections import defaultdict 
#open the file and parse it into a list of strings on newlines
text_file = open("input.txt", "r")
lines = text_file.read().split('\n')

#every input text file has an empty newline at the end, delete it
lines.pop(-1)

for i in range(0, len(lines)):
    lines[i] = int(lines[i])

lines = sorted(lines)

#semi shamelessly stolen from someone in a 4chan thread, he gave way too detailed of a hint
dictionary = defaultdict(int)
dictionary[0] = 1
for i in lines:
    dictionary[i] += dictionary[i - 1] + dictionary[i - 2] + dictionary[i - 3]

print(dictionary[lines[len(lines) - 1]])
print("--- %s seconds ---" % (time.time() - start_time))
