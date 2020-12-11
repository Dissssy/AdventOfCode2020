import time
start_time = time.time()
#open the file and parse it into a list of strings on newlines
text_file = open("input.txt", "r")
lines = text_file.read().split('\n')

#every input text file has an empty newline at the end, delete it
lines.pop(-1)

#convert our input to a 2d list of bools rather than a list of strings
formatted = [[None for i in range(len(lines[0]))] for j in range((len(lines)))]
for i in range(0, len(lines)):
    for j in range(0, len(lines[0])):
        if(lines[i][j] == '#'):
            formatted[i][j] = True
        else:
            formatted[i][j] = False

#initialize some variables needed for the loop
slope = [1, 3]
count = 0
i = 0
j = 0
#using while loops because i dont know if theres any funny business with for loops
#im an idiot, i couldve used the step thing in the range thing damnit
#anyways here we step through the designated slope, checking if we hit a tree or not
#once we hit the right edge we just loop back around
while(i < len(formatted)):
    if formatted[i][j]:
        count += 1
    j += slope[1]
    if j >= len(formatted[0]):
        j -= len(formatted[0])
    i += slope[0]

#print the output     
print(count)
print("--- %s seconds ---" % (time.time() - start_time))
