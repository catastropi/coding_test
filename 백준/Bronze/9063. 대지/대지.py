i = int(input())

array, array2 = [], []

for k in range(0, i):
  a, b = map(int, input().split())
  array.append(a)
  array2.append(b)

print((max(array)-min(array))*(max(array2)-min(array2)))