import re

def mul(a,b):
    return a*b

result = 0
execute = True

with open('data/day3.txt') as file:  
    for line in file: 
        matches = re.findall(r"(mul[(]\d*,\d*[)]|do[(][)]|don't[(][)])", line)
        print(matches)
        for match in matches:
            if match == "do()":
                execute = True
            elif match == "don't()":
                execute = False
            elif execute:
                result += eval(match)

print(result)