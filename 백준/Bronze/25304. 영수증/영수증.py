money = int(input())
k = int(input())
o = 0

for i in range(1, k+1):
  a, b = input().split()
  c = int(a)*int(b)
  o += c

if money == o:
  print("Yes")
else:
  print("No")