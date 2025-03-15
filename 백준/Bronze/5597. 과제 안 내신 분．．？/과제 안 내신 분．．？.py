array = []

for k in range(1, 31):
  array.append(k)

array2 = []

for k in range(1, 29):
  y = int(input())
  array2.append(y)

for k in range(1, len(array2)+1):
  for i in range(1, len(array)+1):
    if array2[k-1] == array[i-1]:
      array.remove(array[i-1])
      array.append(0)

  

for k2 in range(0, 2):
  print(array[k2])