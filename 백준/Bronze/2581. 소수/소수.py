array = []

M = int(input())
N = int(input())

if M <= 2 and N >= 2:
  array.append(2)

for r in range(M, N+1):
  for k in range(2, r):
    if r % k == 0:
      break
    else:
      if k == r-1:
        if r % (r-1) == 0:
          break
        else:
          array.append(r)
          break

if len(array) == 0:
  print(-1)
else:
  print(sum(array))
  print(min(array))