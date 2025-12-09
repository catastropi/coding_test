N = int(input())

List = []

for i in range(N):
  Z = int(input())
  List.append(Z)

List.sort()

for n in range(N):
  print(List[n])