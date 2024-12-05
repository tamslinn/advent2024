import csv

total = 0
rules = []
data = []

with open('data/day5rules.txt') as file:  
    reader = csv.reader(file, delimiter = "|")
    for row in reader:
       rules.append(row)

with open('data/day5data.txt') as file:  
    reader = csv.reader(file, delimiter = ",")
    for row in reader:
       data.append(row)

for line in data:
    correct = True
    for rule in rules:
        try:
            idx1 = line.index(rule[0])
            idx2 = line.index(rule[1])
            if idx2 < idx1:
                correct = False
        except:
            pass

    if correct:
        total += int(line[int((len(line) - 1)/2)])

print(total)