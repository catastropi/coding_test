N = int(input())

tt = [0] * 10001

for z in range(N):
    tt[int(input())] += 1

for i2 in range(1, 10001):
  if tt[i2] > 0:
    for i in range(tt[i2]):
      print(i2)
