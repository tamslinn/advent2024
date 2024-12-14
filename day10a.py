data = []
trailheads = []

isPart2 = True
# read file and count rows
with open('data/day10.txt') as file:  
    for idy, line in enumerate(file): 
        data.append(list(line.rstrip('\n')))
        for idx, val in enumerate(line):
            if val == "0":
                trailheads.append([idx, idy])

directions = [[-1,0],[1,0],[0,-1],[0,1]]

maxX = len(data[0])
maxY = len(data)

def inRange(x,y):
    return 0<= x < maxX and 0 <= y < maxY

def getPaths(nextVal, points):
    paths = []
    for point in points:
        for dir in directions:
            newX = point[0] + dir[0]
            newY = point[1] + dir[1]            
            if inRange(newX,newY) and int(data[newY][newX]) == nextVal:    
                if  [newX,newY] not in paths or isPart2:           
                    paths.append([newX,newY])
    if nextVal == 9:
        return paths
    else:               
        return getPaths(nextVal+1,paths)

score = 0

for trailhead in trailheads:
    paths = getPaths(1, [trailhead])
    score += len(paths)
   
print(score)
