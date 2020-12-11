from copy import deepcopy
import time
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

def countdirection(x, y, grid, direction):
    directions = [(direction % 3) - 1, int((direction - (direction % 3)) / 3) - 1]
    offset = directions.copy()
    chairfound = False
    chairvalue = False
    while((not chairfound) and (0 < (x + offset[0]) < len(grid)) and (0 < (y + offset[1]) < len(grid[0]))):
        if grid[x + offset[0]][y + offset[1]][0]:
            chairfound = True
            chairvalue = grid[x + offset[0]][y + offset[1]][1]
        else:
            offset[0] += directions[0]
            offset[1] += directions[1]
    return chairvalue

def countadjacent(x, y, grid):
    return(countdirection(x, y, grid, 0) +
           countdirection(x, y, grid, 1) + 
           countdirection(x, y, grid, 2) + 
           countdirection(x, y, grid, 3) + 
           countdirection(x, y, grid, 5) + 
           countdirection(x, y, grid, 6) + 
           countdirection(x, y, grid, 7) + 
           countdirection(x, y, grid, 8))

for i in range(0, len(lines)):
    for j in range(0, len(lines[i])):
        if(lines[i][j] == 'L'):
            grid[i + 1][j + 1][0] = True

newgrid = deepcopy(grid)
changed = True
start_time = time.time()
while changed:
    for i in range(0, len(lines)):
        for j in range(0, len(lines[0])):
            x = i + 1
            y = j + 1
            if grid[x][y][0]:
                adjacent = countadjacent(x, y, grid)
                if grid[x][y][1] == False and adjacent == 0:
                    newgrid[x][y][1] = True
                elif grid[x][y][1] == True and adjacent >= 5:
                    newgrid[x][y][1] = False
    #makereadable(grid)
    if(newgrid == grid):
        changed = False
    grid = deepcopy(newgrid)

count = 0
for i in range(0, len(lines)):
    for j in range(0, len(lines[0])):
        if grid[i + 1][j + 1][0]:
            if grid[i + 1][j + 1][1]:
                count += 1
print("--- %s seconds ---" % (time.time() - start_time))
#makereadable(grid)
print(count)

