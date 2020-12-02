text_file = open("input.txt", "r")
lines = text_file.read().split('\n')

lines.pop(-1)

for i in range(0, len(lines)): 
    lines[i] = int(lines[i]) 

v = len(lines)
i = 0
while i < v:
    j = i + 1
    while j < v:
        value = lines[i] + lines[j]
        if value == 2020:
            print(lines[i] * lines[j])
            exit()
        j += 1
    i += 1
