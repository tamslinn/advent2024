f = open("data/day11.txt", "r")
input = (f.readline().split())

counts = [1 for i in range(len(input))] 

for i in range(75):
    newInput = []
    newCounts = []

    def addValue(v, c):
        if v in newInput:
            pos = newInput.index(v)
            newCounts[pos] = newCounts[pos] + c
        else:
            newInput.append(v)
            newCounts.append(c)

    for i, val in enumerate(input):
        if val == "0":
            addValue("1", counts[i])
        elif len(val) % 2 == 0:
            middle = int(len(val)/2)
            addValue(val[0:middle],counts[i])
            addValue(str(int(val[middle:len(val)])),counts[i])
        else:
            addValue(str(int(val)*2024),counts[i])
    input = newInput
    counts = newCounts


print(sum(newCounts))