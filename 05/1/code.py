#open the file and parse it into a list of strings on newlines
text_file = open("input.txt", "r")
lines = text_file.read().split('\n')

#every input text file has an empty newline at the end, delete it
lines.pop(-1)

decimal = [0]*len(lines)
for i in range(0, len(lines)):
    lines[i] = lines[i].replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1')
    for j in range(0, len(lines[i])):
        decimal[i] += (int(lines[i][j]) % 10) * pow(2, 9 - j)

largest = 0
for i in range(0, len(decimal)):
    if(decimal[i] > largest):
        largest = decimal[i]

print(largest)
