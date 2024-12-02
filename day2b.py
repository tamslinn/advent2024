count=0

f = open("data/day2.txt", "r")
for x in f:

  result = False
  row = x.split()
  data = list(map(int, row))

  for i in range(len(data)):
    
    #Make a copy missing one value. Not an efficient approach!
    dataCopy = data.copy()
    del(dataCopy[i])

    desc = all(1 <= dataCopy[i] - dataCopy[i + 1] <= 3 for i in range(len(dataCopy) - 1))
    asc = all(1 <= dataCopy[i+1] - dataCopy[i] <= 3 for i in range(len(dataCopy) - 1))

    if desc or asc:
      result = True

  if result:
    count+=1

print(count)
    
 
