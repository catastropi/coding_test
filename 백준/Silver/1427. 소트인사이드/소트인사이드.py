N = str(input())

l = []

for i in range(len(N)):
  l.append(int(N[i]))

l.sort(reverse=True)
L = ''.join(map(str, l))

print(L)