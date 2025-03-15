a, b, c = input().split()
A, B, C = int(a), int(b), int(c)
money = 0

if A == B == C:
  money = 10000 + A*1000
elif A == B:
  money = 1000 + A * 100
elif C == B:
  money = 1000 + B * 100
elif A == C:
  money = 1000 + C * 100
else:
  money = max(A, B, C) * 100

print(money)
