from copy import deepcopy
import time
start_time = time.time()
#open the file and parse it into a list of strings on newlines
text_file = open("input.txt", "r")
lines = text_file.read().split('\n')

#every input text file has an empty newline at the end, delete it
lines.pop(-1)

grid = [[[False, False] for i in range(len(lines[0]) + 2)] for i in range(len(lines) + 2)]

def makereadable(grid):
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if grid[i][j][0]:
                if grid[i][j][1]:
                    print("#", end="")
                else:
                    print("L", end="")
            else:
                print(".", end="")
        print("")

for i in range(0, len(lines)):
    for j in range(0, len(lines[i])):
        if(lines[i][j] == 'L'):
            grid[i + 1][j + 1][0] = True

newgrid = deepcopy(grid)
changed = True
while changed:
    #makereadable(grid)
    for i in range(0, len(lines)):
        for j in range(0, len(lines[0])):
            if grid[i + 1][j + 1][0]:
                if grid[i + 1][j + 1][1] == False and grid[i][j][1] + grid[i + 1][j][1] + grid[i + 2][j][1] + grid[i][j + 1][1] + grid[i + 2][j + 1][1] + grid[i][j + 2][1] + grid[i + 1][j + 2][1] + grid[i + 2][j + 2][1] == 0:
                    newgrid[i + 1][j + 1][1] = True
                elif grid[i + 1][j + 1][1] == True and grid[i][j][1] + grid[i + 1][j][1] + grid[i + 2][j][1] + grid[i][j + 1][1] + grid[i + 2][j + 1][1] + grid[i][j + 2][1] + grid[i + 1][j + 2][1] + grid[i + 2][j + 2][1] >= 4:
                    newgrid[i + 1][j + 1][1] = False    
    if(newgrid == grid):
        changed = False
    grid = deepcopy(newgrid)

count = 0
for i in range(0, len(lines)):
    for j in range(0, len(lines[0])):
        if grid[i + 1][j + 1][0]:
            if grid[i + 1][j + 1][1]:
                count += 1

#makereadable(grid)
print(count)
print("--- %s seconds ---" % (time.time() - start_time))
