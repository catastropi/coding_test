a, b = input().split()

array, array2, total = [], [], []

for i in range(1, int(a)+1):
  z = input().split()
  array.append(z)

for p in range(1, int(a)+1):
  z2 = input().split()
  array2.append(z2)

for t in range(0, int(a)):
  for o in range(0, int(b)):
    total.append(int(array[t][o])+int(array2[t][o]))

n = 0
for t in range(0, int(a)):
  for o in range(0, int(b)):
    print(total[n], end = " ")
    n += 1
  print()