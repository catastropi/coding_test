a, b = map(int, input().split())

array, k = 10000 * [0], 0

for u in range(1, a+1):
  if a % u == 0:
    array[k] = u
    k += 1

print(array[b-1])
