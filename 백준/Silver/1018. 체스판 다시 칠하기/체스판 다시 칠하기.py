M, N = map(int, input().split())

array, X, Y = [], 0, 0
for b in range(M):
  s = list(str(input()))
  array.append(s)

zarray = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], 
          ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], 
          ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], 
          ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], 
          ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], 
          ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], 
          ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], 
          ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]

Zarray = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], 
          ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], 
          ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], 
          ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], 
          ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], 
          ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], 
          ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], 
          ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]


A, B, a, b, marray = 0, 8, 0, 8, []
for _ in range((M-7)):
  for _ in range((N-7)):
    for i in range(A, B):
      for v in range(a, b):
        if array[i][v] != zarray[i-A][v-a]:
          X += 1
        if array[i][v] != Zarray[i-A][v-a]:
          Y += 1  
    marray.append(X)
    marray.append(Y)
    X, Y = 0, 0
    a += 1
    b += 1
  a, b = 0, 8
  A += 1
  B += 1

print(min(marray))