a, b = input().split()
C = int(input())

A, B = int(a), int(b)
H, M = 0, 0

if B + C >= 60:
  M = (B + C) - 60*((B+C)//60)
  if A + (B + C)//60 >= 24:
    H = A + (B + C)//60 - 24
  else:
    H = A + (B + C)//60
else:
  M = B + C
  H = A + (B+C)//60

print(int(H), int(M))