import itertools
import math

count=0
f = open("data/day8.txt", "r")

input = []
data = []
results = []



maxY = 0
for y, line in enumerate(f):
    maxY += 1
    row = list(line.rstrip('\n'))
    input.append(row)
    maxX = len(row)
    for x, val in enumerate(row):
        if val != '.':
            data.append([val, x, y])

combs = itertools.combinations(data,2)

def inRange(x, y):
    return x >= 0 and y >= 0 and x < maxX and y < maxY

def addPoint(x,y, val):
   if [int(x),int(y)] not in results:
      results.append([int(x),int(y)])
      input[int(y)][int(x)] = val

for (a,b) in combs:
    if a[0] == b[0]:
        diffX = a[1] - b[1]
        diffY = a[2] - b[2]

        gcf = math.gcd(diffX, diffY)
        
        x = a[1]
        y = a[2]

        stepX = diffX/gcf
        stepY = diffY/gcf

        while inRange(x,y):
            addPoint(x,y, a[0])
            x -= stepX
            y -= stepY

        x = a[1]
        y = a[2]
        while inRange(x,y):
            addPoint(x,y, a[0])
            x += stepX
            y += stepY
       
print(len(results))      
       
