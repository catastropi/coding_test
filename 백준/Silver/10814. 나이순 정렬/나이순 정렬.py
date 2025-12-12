N = int(input()) 

arr = []

for i in range(N):
  xy = list(input().split())
  xy[0] = int(xy[0])
  xy[1] = str(i) + '.' + xy[1] 
  arr.append(xy)

arr.sort(key=lambda x: x[0])

for t in range(N):
  for z in range(len(arr[t][1])):
    if arr[t][1][z] == '.':
      arr[t][1] = arr[t][1][z+1:]
      break

for d in range(N):
  print(str(arr[d][0]) + " " + str(arr[d][1]))
