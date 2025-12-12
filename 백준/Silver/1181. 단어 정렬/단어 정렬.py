N = int(input())

arr = []

for i in range(N):
  S = str(input())
  arr.append(S)

arr2 = set(arr)
arr3 = list(arr2)

arr3.sort()
A = []

for y in range(1, 51):
  for t in arr3:
    if len(t) == y:
      A.append(t)

for r in range(len(A)):
  print(A[r])