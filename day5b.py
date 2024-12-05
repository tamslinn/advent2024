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

def testData(data):
    correct = True
    for rule in rules:
        try:
            idx1 = data.index(rule[0])
            idx2 = data.index(rule[1])
            if idx2 < idx1:
                correct = False
        except:
            pass
    return correct

def compare(a, b):
    result = 0
    for rule in rules:
        if rule[0] == a and rule[1] == b:
            result = -1
        elif rule[0] == b and rule[1] == a:
            result = 1
    return result

def sortLine(data):
    for i in range(1, len(data)):
        item = data[i]
        j = i - 1
        while j >= 0 and compare(data[j], item) == 1:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = item

    return data

for line in data:
    if not testData(line):
        newLine = sortLine(line)
        print(newLine)


        total += int(newLine[int((len(newLine) - 1)/2)])

print(total)