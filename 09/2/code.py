import time
start_time = time.time()
#open the file and parse it into a list of strings on newlines
text_file = open("input.txt", "r")
lines = text_file.read().split('\n')

#every input text file has an empty newline at the end, delete it
lines.pop(-1)

def isvalid(i):
    for j in range(i - 25, i):
        for l in range(j + 1, i):
            if(lines[j] + lines[l] == lines[i]):
                return True
    return False

def check():
    for i in range(2, len(lines)):
        for j in range(0, len(lines) - i):
            check = [None]*i
            sum = 0
            for l in range(j, j + i):
                check[l - j] = lines[l]
            for l in range(0, len(check)):
                sum += check[l]
            if(sum == invalid):
                return(min(check) + max(check))

for i in range(0, len(lines)):
    lines[i] = int(lines[i])

for i in range(25, len(lines)):
    if not isvalid(i):
        invalid = lines[i]

print(check())
print("--- %s seconds ---" % (time.time() - start_time))
