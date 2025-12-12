N = int(input())

Array = []

for i in range(N):
  xy = list(map(int,input().split()))
  xi, yi = xy[0], xy[1]
  xy[0], xy[1] = yi, xi
  Array.append(xy)

Array.sort()

for t in range(N):
  print(str(Array[t][1]) + " " + str(Array[t][0]))