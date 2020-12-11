import time
start_time = time.time()
#open the file and parse it into a list of strings on newlines
text_file = open("input.txt", "r")
lines = text_file.read().split('\n')

#every input text file has an empty newline at the end, delete it
lines.pop(-1)

decimal = [0]*len(lines)
for i in range(0, len(lines)):
    lines[i] = lines[i].replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1')
    for j in range(0, len(lines[i])):
        decimal[i] += (int(lines[i][j]) % 10) * pow(2, (len(lines[0]) - 1) - j)

sort = sorted(decimal)
processed = []
for i in range(0, len(sort) - 2):
    if not (sort[i] == sort[i + 1] - 1 and sort[i + 1] - 1 == sort[i + 2] - 2):
        processed.append(sort[i])

final = []
for i in range(0, len(processed), 2):
    final.append(processed[i] + 2)

print(final)
print("--- %s seconds ---" % (time.time() - start_time))
