p = list(map(int, input().split()))

M = max(p)
p.pop(p.index(max(p)))
if sum(p) > M:
  p.append(M)
  print(sum(p))
else:
  M = sum(p)-1
  p.append(M)
  print(sum(p))