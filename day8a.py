import itertools

count=0

f = open("data/day8.txt", "r")

data = []
results = []

maxY = 0
for y, line in enumerate(f):
    maxY += 1
    row = list(line.rstrip('\n'))
    maxX = len(row)
    for x, val in enumerate(row):
       if val != ".":
         data.append([val, x, y])

combs = itertools.combinations(data,2)

def addPoint(x,y):
   if x >= 0 and y >= 0 and x < maxX and y < maxY and [x,y] not in results:
      results.append([x,y])

for (a,b) in combs:
    if a[0] == b[0]:
        diffX = a[1] - b[1]
        diffY = a[2] - b[2]
        if diffX/3 % 1 == 0 and diffY/3 % 1 == 0:
            addPoint(a[1] + diffX/3, a[2] + diffY/3)
            addPoint(a[1] + 2* diffX/3, a[2] + 2 * diffY/3)

        addPoint(a[1] + diffX, a[2] + diffY)
        addPoint(b[1] - diffX, b[2] - diffY)

print(len(results))      
       
