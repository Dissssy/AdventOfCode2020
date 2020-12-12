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
        return [[True, int(int(instruction.replace("R", "")) / 90)]]
    elif "L" in instruction:
        return [[False, int(int(instruction.replace("L", "")) / 90)]]
    elif "F" in instruction:
        return [[int(instruction.replace("F", ""))]]

#east:  +x
#west:  -x
#north: +y
#south: -y
x = 10
y = 1
shipx = 0
shipy = 0

for i in range(0, len(lines)):
    instruction = parse(lines[i])
    ident = len(instruction) + len(instruction[0])
    if ident == 4:
        x += instruction[0][0] * instruction[1]
        y += instruction[0][1] * instruction[1]
    elif ident == 3:
        increments = instruction[0][1]
        if instruction[0][0]:
            increments = 4 - increments
        for i in range(0, increments):
            tmp = x
            x = -y
            y = tmp
    elif ident == 2:
        shipx += x * instruction[0][0]
        shipy += y * instruction[0][0]

print(abs(shipx) + abs(shipy))
print("--- %s seconds ---" % (time.time() - start_time))
