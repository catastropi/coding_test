p = int(input())

n = 4

for i in range(p):
  n = ((n**0.5) * (2) - 1) ** 2

print(int(n))