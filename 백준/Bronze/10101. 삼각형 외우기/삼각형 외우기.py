array = []

for k in range(3):
  i = int(input())
  array.append(i)

s = sum(array)

if s == 180:
  if array[0] == array[1] == array[2]:
    print('Equilateral')
  elif array[0] == array[1] or array[0] == array[2] or array[1] == array[2]:
    print('Isosceles')
  elif array[0] != array[1] != array[2]:
    print('Scalene')
else:
  print('Error')
