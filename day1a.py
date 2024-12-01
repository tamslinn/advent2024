import csv

col1 = []
col2 = []
  
with open('data/day1a.txt') as file:
      
    reader = csv.reader(file, delimiter = " ")
    for row in reader:
       col1.append(int(row[0]))
       col2.append(int(row[3]))

col1.sort()
col2.sort()

total = 0

for idx, x in enumerate(col1):
    total += abs(x - col2[idx])

print(total)

