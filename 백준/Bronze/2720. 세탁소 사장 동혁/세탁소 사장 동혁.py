i = int(input())

for j in range(i):
  j = int(input())
  l, lis = 0, [0, 0, 0, 0]
  while j > 0:
    if j >= 25:
      while j - (25 * l) > 0:
        l += 1
        if l * 25 > j:
          l -= 1
          j -= (25 * l)
          lis[0] = l
          l = 0
          break
        elif l * 25 == j:
          j -= (25 * l)
          lis[0] = l
          l = 0
          break
    elif j >= 10:
      while j - (10 * l) > 0:
        l += 1
        if l * 10 > j:
          l -= 1
          j -= (10 * l)
          lis[1] = l
          l = 0
          break
        elif l * 10 == j:
          j -= (10 * l)
          lis[1] = l
          l = 0
          break
    elif j >= 5:
      while j - (5 * l) > 0:
        l += 1
        if l * 5 > j:
          l -= 1
          j -= (5 * l)
          lis[2] = l
          l = 0
          break
        elif l * 5 == j:
          j -= (5 * l)
          lis[2] = l
          l = 0
          break
    elif j >= 1:
      while j - (1 * l) > 0:
        l += 1
        if l * 1 > j:
          l -= 1
          j -= (1 * l)
          lis[3] = l
          l = 0
          break
        elif l * 1 == j:
          j -= (1 * l)
          lis[3] = l
          l = 0
          break
  for iz in lis:
    print(iz, end = " ")
  lis = [0, 0, 0, 0]