count=0

f = open("data/day2a.txt", "r")
for x in f:
  row = x.split()
  data = list(map(int, row))
  

  desc = all(1 <= data[i] - data[i + 1] <= 3 for i in range(len(data) - 1))
  asc = all(1 <= data[i+1] - data[i] <= 3 for i in range(len(data) - 1))

  if desc or asc:
    count+=1

print(count)

