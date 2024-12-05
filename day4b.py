import re

count = 0
data = []

# read file and count rows
with open('data/day4.txt') as file:  
    for line in file: 
        data.append(list(line.rstrip('\n')))

def isMS(val):
    return val in ('M','S')

def isXmas(tl,tr,m,bl,br):

    if m != 'A':
        return False
    if not (isMS(tl) and isMS(tr) and isMS(bl) and isMS(br)):
        return False
    if tl == 'M' and br != 'S':
        return False
    if tl == 'S' and br != 'M':
        return False
    if tr == 'M' and bl != 'S':
        return False
    if tr == 'S' and bl != 'M':
        return False
    
    print("")
    print(tl + "." + tr)
    print("." + m + ".")
    print(bl + "." + br)
    
    return True


#loop through looking for patterns
for y, row in enumerate(data):
    if (y < len(data) - 2):
        for x in range(len(data[0]) - 2):
            if isXmas(row[x],row[x+2],data[y+1][x+1],data[y+2][x],data[y+2][x+2]):
                #print(str(x) + "," + str(y))
                count+=1

print(count)
