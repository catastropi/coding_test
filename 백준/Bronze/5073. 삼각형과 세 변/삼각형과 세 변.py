while True:
  a = list(map(int, input().split()))
  if a[1] == a[2] == a[0] == 0:
    break
  else:
    array = []
    for y in range(3):
      array.append(a[y])
    M = max(array)
    array.pop(array.index(max(array))) 
    if M >= sum(array):
      print('Invalid')
    else:
      if a[1] == a[2] == a[0]:
        print('Equilateral')
      elif a[0] == a[1] or a[0] == a[2] or a[1] == a[2]:
        print('Isosceles')
      elif a[0] != a[1] != a[2]:
        print('Scalene')
