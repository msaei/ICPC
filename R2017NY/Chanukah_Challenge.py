def candle(n):
  result = n*(n+1)//2 + n
  return result
x = ""
x = input(x)
line = []
for i in range(int(x)):
  line.append(input())

for l in line:
  [r, n] = l.split()
  print(r, candle(int(n)))