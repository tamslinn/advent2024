
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
    elif yDir == 1:
        yDir = 0
        xDir = -1
    elif xDir == 1:
        yDir = 1
        xDir = 0
    else:
        yDir = -1
        xDir = 0
    return [xDir, yDir]

# find start
for idy, row in enumerate(data):
    for idx, val in enumerate(row):
        if val == '^':
            x = idx
            y = idy
            break

xDir = 0
yDir = -1
count = 1
data[y][x] = "X"

while not atEdge(x,y):
    nextVal = data[y + yDir][x + xDir]
    if nextVal == ".":
        count += 1
    if nextVal in (".","X"):
        y = y+yDir
        x = x+xDir
        data[y][x] = "X"
    else:
        [xDir, yDir] = turnRight(xDir, yDir)
        
print(count)

