f = open("data/day9.txt", "r")
input = list(f.readline())

id = 0
inputPos = 0
isSpace = False
data = []

while inputPos < len(input):
    count = int(input[inputPos])
    if isSpace:
        data.extend(["."] * count)
    else :
        data.extend([str(id)] * count)
        id += 1
    isSpace = not isSpace
    inputPos += 1

writePos = 0

while data[writePos] != ".":
    writePos += 1

readPos = len(data) - 1

while readPos >= 0 and readPos > writePos:
    if data[readPos] != ".":
        data[writePos] = data[readPos]
        data[readPos] = "."
        while writePos < len(data) and data[writePos] != ".":
            writePos += 1
    readPos -= 1

hash = 0
for idx, val in enumerate(data):
    if val != ".":
        hash += idx * int(val)

print(hash)



