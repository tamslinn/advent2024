import copy

data = []

# read file and count rows
with open('data/day6.txt') as file:  
    for line in file: 
        data.append(list(line.rstrip('\n')))

maxY = len(data) - 1
maxX = len(data[0]) - 1

def atEdge(x,y):
    return x == 0 or y == 0 or x == maxX or y == maxY

def turnRight(xDir, yDir):
    if yDir == -1:
        yDir = 0
        xDir = 1
        curDir = "R"
    elif yDir == 1:
        yDir = 0
        xDir = -1
        curDir = "L"
    elif xDir == 1:
        yDir = 1
        xDir = 0
        curDir = "D"
    else:
        yDir = -1
        xDir = 0
        curDir = "U"
    return [xDir, yDir, curDir]

def isFree(val):
    for s in (".","U","D","L","R"):
        if s in val:
            return True
    return False

def couldLoop(dataCopy, xDir,yDir, x, y):
   
    dataCopy[y + yDir][x + xDir] = '@'
    # turn
    [xDir1, yDir1, dir] = turnRight(xDir,yDir)

    x1 = x
    y1 = y
    dataCopy[y1][x1] = dir

    while not atEdge(x1,y1):

        nextVal = dataCopy[y1 + yDir1][x1 + xDir1]
        
        if dir in nextVal:
            return True
        elif isFree(nextVal):
            y1 = y1+yDir1
            x1 = x1+xDir1
            if nextVal == ".":
                dataCopy[y1][x1] = dir
            else:
                dataCopy[y1][x1] = dataCopy[y1][x1] + dir
        else:
            [xDir1, yDir1, dir] = turnRight(xDir1, yDir1)
        
    return False

# find start
for idy, row in enumerate(data):
    for idx, val in enumerate(row):
        if val == '^':
            x = idx
            y = idy
            break

curDir = "U"
xDir = 0
yDir = -1

data[y][x] = curDir
count = 0

while not atEdge(x,y):
    nextVal = data[y + yDir][x + xDir]
    if nextVal == "." and couldLoop(copy.deepcopy(data), xDir,yDir, x, y):
        count+=1
    
    if nextVal in (".","U","D","L","R"):
        data[y][x] = curDir
        y = y+yDir
        x = x+xDir
    else:
        [xDir, yDir, curDir] = turnRight(xDir, yDir)
        data[y][x] = curDir

print(count)

