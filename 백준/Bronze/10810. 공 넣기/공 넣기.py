N, M = input().split()

array = []

for I in range(1, int(N)+1):
  array.append(0)

for I in range(1, int(M)+1):
  i, j, k = input().split()
  for m in range(int(i), int(j)+1):
    array[m-1] = int(k)
  
for o in array:
  print(o, end = " ")