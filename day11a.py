f = open("data/day11.txt", "r")
input = (f.readline().split())

for i in range(25):
    newInput = []
    for val in input:
        if val == "0":
            newInput.append("1")
        elif len(val) % 2 == 0:
            middle = int(len(val)/2)
            newInput.append(val[0:middle])
            newInput.append(str(int(val[middle:len(val)])))
        else:
            newInput.append(str(int(val)*2024))

    input = newInput


print(len(input))