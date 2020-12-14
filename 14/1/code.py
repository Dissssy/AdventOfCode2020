import time
start_time = time.time()
#open the file and parse it into a list of strings on newlines
text_file = open("input.txt", "r")
lines = text_file.read().split('\n')

#every input text file has an empty newline at the end, delete it
lines.pop(-1)

def binarystr(number):
    yield number % 2
    yield from binarystr(int(number / 2))

def tobinary(number, length):
    binary = binarystr(number)
    final = ""
    for i in range(0, length):
        final = str(next(binary)) + final        
    return final

def todecimal(binarystring):
    decimal = 0
    for i in range(len(binarystring), 0, -1):
        if binarystring[i - 1] == "1":
            decimal += pow(2, len(binarystring) - i)
    return decimal

def applymask(binarynum, mask):
    if not len(binarynum) == len(mask):
        print(f"binarynum {len(binarynum)} is not the same length as mask {len(mask)}")
        return None
    masked = ""
    for i in range(0, len(mask)):
        if mask[i] == "X":
            masked += binarynum[i]
        else:
            masked += mask[i]
    return todecimal(masked)

for i in range(0, len(lines)):
    lines[i] = lines[i].split(" = ")

memory = {}

for i in range(0, len(lines)):
    if "mask" in lines[i][0]:
        mask  = lines[i][1]
    else:
        memory[lines[i][0].replace("mem[", "").replace("]", "")] = applymask(tobinary(int(lines[i][1]), len(mask)), mask)

out = 0
for i in memory.keys():
    out += memory[i]

print(out)
print("--- %s seconds ---" % (time.time() - start_time))
