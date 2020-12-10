#open the file and parse it into a list of strings on newlines
text_file = open("input.txt", "r")
lines = text_file.read().split('\n')

#every input text file has an empty newline at the end, delete it
lines.pop(-1)

for i in range(0, len(lines)):
    lines[i] = int(lines[i])

lines = sorted(lines)

count = [0]*3
count[lines[0] - 0 - 1] += 1

for i in range(0, len(lines) - 1):
    count[lines[i + 1] - lines[i] - 1] += 1

count[2] += 1

print(f"{count[0]} * {count[2]} = {count[0] * count[2]}")
