N = int(input())

Array = []

for i in range(N):
  xy = list(map(int,input().split()))
  Array.append(xy)

Array.sort()

for t in range(N):
  print(str(Array[t][0]) + " " + str(Array[t][1]))