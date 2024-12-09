f = open("data/day9.txt", "r")
input = list(f.readline())

id = 0
data = []
i = 0
isSpace = False
while i <= len(input)-1:
    if isSpace:
        data.append([input[i], "."])
    else:
        data.append([input[i], str(id)])
        id += 1
    isSpace = not isSpace    
    i+= 1

readPos = len(data) -1  
while readPos >= 1:
    if data[readPos][1] != "." and len(data[readPos]) == 2:
        writePos = 1
        while writePos < readPos:
            
            if data[writePos][1] == "." and len(data[writePos]) == 2 and int(data[writePos][0]) >= int(data[readPos][0]):
                space = int(data[writePos][0])
                data[writePos] = [data[readPos][0],data[readPos][1],'X']
                data[readPos][1] = "."
                if space > int(data[readPos][0]):
                    data.insert(writePos + 1, [space - int(data[readPos][0]),"."])
                    readPos += 1
                
                break
            writePos += 1

    readPos -= 1

hash = 0
i = 0
for val in data:
    for j in range(int(val[0])):
        if val[1] != ".":
            hash += i * int(val[1])
        i += 1

print(hash)