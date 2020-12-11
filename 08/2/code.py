import time
start_time = time.time()
#open the file and parse it into a list of strings on newlines
text_file = open("input.txt", "r")
instructions = text_file.read().split('\n')

#every input text file has an empty newline at the end, delete it
instructions.pop(-1)

for i in range(0, len(instructions)):
    instructions[i] = instructions[i].split(" ")

def solve(solveinstructions):
    acc = 0
    i = 0
    result = [None]*2
    check = [0]*len(solveinstructions)

    while(check[i] == 0):
        check[i] += 1
        if(solveinstructions[i][0] == "nop"):
            i += 1
        elif(solveinstructions[i][0] == "acc"):
            acc += int(solveinstructions[i][1])
            i += 1
        elif(solveinstructions[i][0] == "jmp"):
            i += int(solveinstructions[i][1])
        else:
            print(f"what is {solveinstructions[i][0]}")
        if i >= len(solveinstructions):
            return acc, True
    return acc, False

j = 0

out = solve(instructions)
done = out[1]

while j < len(instructions) and done == False:
    newinstructions = [x[:] for x in instructions]
    solving = False
    if(newinstructions[j][0] == "nop"):
        newinstructions[j][0] = "jmp"
        solving = True
    elif(newinstructions[j][0] == "jmp"):
        newinstructions[j][0] = "nop"
        solving = True
    if solving:
        out = solve(newinstructions)
    done = out[1]
    j += 1

print(out[0])
print("--- %s seconds ---" % (time.time() - start_time))
