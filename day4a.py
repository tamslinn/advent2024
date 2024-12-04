import re

count = 0
data = []

# read file and count rows
with open('data/day4.txt') as file:  
    for line in file: 
        count+= len(re.findall(r"XMAS", line))
        count+= len(re.findall(r"SAMX", line))
        data.append(list(line.rstrip('\n')))

# count cols
for i in range(len(data[0])):
    col = "".join([row[i] for row in data])
    count+= len(re.findall(r"XMAS", col))
    count+= len(re.findall(r"SAMX", col))

# get diagonals
max_col = len(data[0])
max_row = len(data)
fdiag = [[] for _ in range(max_row + max_col - 1)]
bdiag = [[] for _ in range(len(fdiag))]
min_bdiag = -max_row + 1

for x in range(max_col):
    for y in range(max_row):
        
        fdiag[x+y].append(data[y][x])
        bdiag[x-y-min_bdiag].append(data[y][x])

for line in fdiag:
    str = "".join(line)
    count+= len(re.findall(r"XMAS", str))
    count+= len(re.findall(r"SAMX", str))

for line in bdiag:
    str = "".join(line)
    count+= len(re.findall(r"XMAS", str))
    count+= len(re.findall(r"SAMX", str))

print(count)
