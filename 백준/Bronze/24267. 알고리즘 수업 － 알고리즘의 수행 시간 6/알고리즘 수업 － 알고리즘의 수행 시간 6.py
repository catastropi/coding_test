i = int(input())

array = []

for k in range(1, i-1):
  array.append(k*(i-1-k))

print(sum(array))
print(3)