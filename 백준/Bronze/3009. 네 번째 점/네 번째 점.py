array, array2 = [], []

for i in range(0, 3):  
  x, y = map(int, input().split())
  array.append(x)
  array2.append(y)

X, y = 0, 0

if array[0] == array[1]:
  X = array[2]
elif array[0] == array[2]:
  X = array[1]
elif array[1] == array[2]:
  X = array[0]

if array2[0] == array2[1]:
  Y = array2[2]
elif array2[0] == array2[2]:
  Y = array2[1]
elif array2[1] == array2[2]:
  Y = array2[0]

print(X, Y)