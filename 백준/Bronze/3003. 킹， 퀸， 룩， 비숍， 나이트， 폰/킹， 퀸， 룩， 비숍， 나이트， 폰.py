chess = input().split()
array = [1, 1, 2, 2, 2, 8]
array2 = []

for i in range(0, len(chess)):
  array2.append(array[i] - int(chess[i]))

for h in array2:
  print(h, end = " ")