#open the file and parse it into a list of strings on newlines
text_file = open("input.txt", "r")
lines = text_file.read().split('\n')

#every input text file has an empty newline at the end, delete it
lines.pop(-1)

#define the checkslope function that i will be using to check each slope
def checkslope(slope,trees):
    j = 0
    count = 0
    for i in range(0, len(trees), slope[0]):
        if trees[i][j % len(trees[0])]:
            count += 1
        j += slope[1]
    return(count)

#convert our input to a 2d list of bools rather than a list of strings
formatted = [[None for i in range(len(lines[0]))] for j in range((len(lines)))]
for i in range(0, len(lines)):
    for j in range(0, len(lines[0])):
        if(lines[i][j] == '#'):
            formatted[i][j] = True
        else:
            formatted[i][j] = False

#calculate and print the output
output = ((checkslope([1,1],formatted)) *
          (checkslope([1,3],formatted)) *
          (checkslope([1,5],formatted)) *
          (checkslope([1,7],formatted)) *
          (checkslope([2,1],formatted)))

print(output)
