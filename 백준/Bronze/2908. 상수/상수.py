List = input().split()

array = []
for i in List:
  a = list(i)
  r = ''.join(reversed(a))
  array.append(int(r))

print(max(array))