import time
start_time = time.time()
#open the file and parse it into a list of strings on newlines
text_file = open("input.txt", "r")
lines = text_file.read().split('\n')

#every input text file has an empty newline at the end, delete it
lines.pop(-1)

def parse(instruction):
    if "N" in instruction:
        return [[0, 1], int(instruction.replace("N", ""))]
    elif "S" in instruction:
        return [[0, -1], int(instruction.replace("S", ""))]
    elif "E" in instruction:
        return [[1, 0], int(instruction.replace("E", ""))]
    elif "W" in instruction:
        return [[-1, 0], int(instruction.replace("W", ""))]
    elif "R" in instruction:
        return [[1, int(int(instruction.replace("R", "")) / 90)]]
    elif "L" in instruction:
        return [[-1, int(int(instruction.replace("L", "")) / 90)]]
    elif "F" in instruction:
        return [[int(instruction.replace("F", ""))]]

#east:  +x
#west:  -x
#north: +y
#south: -y
x = 0
y = 0
#east:  0
#south: 1
#west:  2
#north: 3
d = 0

absolute = dict([(0, [1, 0]),
                 (1, [0, -1]),
                 (2, [-1, 0]),
                 (3, [0, 1])])

for i in range(0, len(lines)):
    instruction = parse(lines[i])
    ident = len(instruction) + len(instruction[0]) - 1
    if ident == 3:
        x += instruction[0][0] * instruction[1]
        y += instruction[0][1] * instruction[1]
    elif ident == 2:
        d += instruction[0][0] * instruction[0][1]
    elif ident == 1:
        x += absolute[d % 4][0] * instruction[0][0]
        y += absolute[d % 4][1] * instruction[0][0]

print(abs(x) + abs(y))
print("--- %s seconds ---" % (time.time() - start_time))
