a = int(input())

grid = [[0] * 100 for _ in range(100)]

for _ in range(0, a):
  b, c = map(int, input().split())
  for i in range(b, b+10):
    for z in range(c, c+10):
      grid[i][z] = 1

count = 0
for g in range(0, 100):
  for g2 in range(0, 100):
    if grid[g][g2] == 1:
      count += 1

print(count)