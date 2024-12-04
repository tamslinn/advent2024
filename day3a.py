import re

def mul(a,b):
    return a*b

result = 0

with open('data/day3.txt') as file:  
    for line in file: 
        matches = re.findall(r"mul[(]\d*,\d*[)]", line)

        for match in matches:
            result += eval(match)

print(result)