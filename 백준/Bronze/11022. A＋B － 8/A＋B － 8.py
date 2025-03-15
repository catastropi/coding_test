k = int(input())

for i in range(1, k+1):
  a, b = input().split()
  A, B = int(a), int(b)
  print("Case #{}: {} + {} = {}".format(i, A, B, A + B))