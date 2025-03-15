array = []

for i in range(1, 10):
  k = int(input())
  array.append(k)

M = max(array)
print(M)
print(array.index(M)+1)