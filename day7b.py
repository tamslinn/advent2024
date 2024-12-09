count=0

f = open("data/day7.txt", "r")

overallResult = 0

def nextSum(i, vals, soFar):
    i += 1

    if i == len(vals):
       return soFar
    else:
        nextResults = []
        for result in soFar:
            nextResults.append(result + vals[i])
            nextResults.append(result * vals[i])
            nextResults.append(int(str(result) + str(vals[i])))
        return nextSum(i, vals, nextResults)

for x in f:
  row = x.split()
  result = int(row[0][0:-1])
  data = list(map(int, row[1:]))
  totals = nextSum(0, data, [data[0]])
  for total in totals:
     if result == total:
        overallResult += result
        break

  
print(overallResult)
