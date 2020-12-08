#open the file and parse it into a list of strings on newlines
text_file = open("input.txt", "r")
instructions = text_file.read().split('\n')

#every input text file has an empty newline at the end, delete it
instructions.pop(-1)

for i in range(0, len(instructions)):
    instructions[i] = instructions[i].split(" ")

acc = 0
i = 0
check = [0]*len(instructions)

while(check[i] == 0):
    check[i] += 1
    if(instructions[i][0] == "nop"):
        i += 1
    elif(instructions[i][0] == "acc"):
        acc += int(instructions[i][1])
        i += 1
    elif(instructions[i][0] == "jmp"):
        i += int(instructions[i][1])
    else:
        print("what")
    if i >= len(check):
        break

print(acc)
